import requests
from scholarly import scholarly
from fuzzywuzzy import fuzz
import os
import time

# --- Step 1: Read Authors List ---
authors_file_path = "/Users/raja/Desktop/DeakinIOT-RAJA/DeakinIOT-RAJA/authors_list.txt"

def normalize_name(name):
    """Normalize a name by removing titles, extra spaces, and converting to lowercase."""
    return name.replace("Dr.", "").replace("Prof.", "").replace("Mr.", "").strip().lower()

with open(authors_file_path, "r") as file:
    known_authors = [normalize_name(line.strip()) for line in file.readlines()]

print(f"Loaded authors: {known_authors}")

# --- Step 2: Define Base Directory for Author Publications ---
BASE_DIR = "content/publication"
os.makedirs(BASE_DIR, exist_ok=True)

# --- Step 3: CrossRef API Function ---
def get_publication_type_from_crossref(title, retries=3, delay=5):
    """
    Fetch publication type using the CrossRef API with retries for failures.
    """
    url = f"https://api.crossref.org/works?query.title={title}"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                items = response.json().get('message', {}).get('items', [])
                if items:
                    return items[0].get('type', 'unknown')
            return 'unknown'
        except requests.RequestException as e:
            print(f"Error fetching CrossRef data for title '{title}' (attempt {attempt + 1}): {e}")
            if attempt < retries - 1:
                time.sleep(delay)
    # Log failures for later debugging
    with open("failed_requests.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"Failed to fetch CrossRef data for title: {title}\n")
    return 'unknown'

# --- Step 4: Categorize Papers ---
def categorize_paper(publication_name, title):
    """
    Categorize papers using CrossRef API or fallback logic.
    Returns numeric value for publication type and the textual label.
    """
    crossref_type = get_publication_type_from_crossref(title)
    if crossref_type == 'unknown':
        print(f"CrossRef data unavailable for title '{title}', falling back to keyword matching.")
    if crossref_type in ["journal-article", "proceedings-article"]:
        return ("2", "Journal Article") if crossref_type == "journal-article" else ("1", "Conference Paper")

    # Fallback: Use venue or title keywords
    lower_pub = (publication_name or "").lower()
    if any(kw in lower_pub for kw in ["conference", "symposium", "proceedings", "workshop"]):
        return ("1", "Conference Paper")  # Conference paper
    elif any(kw in lower_pub for kw in ["journal", "letters", "transactions"]):
        return ("2", "Journal Article")  # Journal article
    return ("3", "Preprint")  # Preprint

def clean_file_name(title):
    """Create a safe filename from the paper title."""
    return title.replace(" ", "_").replace("/", "_").replace(":", "_")[:50]

def author_matches(authors_raw, known_authors, threshold=70):
    """
    Check if any known authors match the publication authors using fuzzy matching.
    """
    authors_list = [normalize_name(author) for author in authors_raw.split(",")]
    for pub_author in authors_list:
        for known_author in known_authors:
            if fuzz.partial_ratio(pub_author, known_author) >= threshold:
                return True  # A close match is found
    return False

# --- Step 5: Fetch Publications for Each Author ---
processed_titles = set()

for author_name in known_authors:
    print(f"Searching for author: {author_name}")
    search_query = scholarly.search_author(author_name)
    try:
        author = next(search_query)
        author = scholarly.fill(author, sections=["publications"])
        print(f"Found author: {author['name']}")
    except StopIteration:
        print(f"Author '{author_name}' not found. Skipping...")
        continue

    # Create folder for the author
    author_folder = os.path.join(BASE_DIR, author_name.replace(" ", "_"))
    os.makedirs(author_folder, exist_ok=True)

    # Process each publication
    for pub in author['publications']:
        scholarly.fill(pub)  # Fetch full details
        
        # Extract paper details
        title = pub.get('bib', {}).get('title', 'Untitled Paper')
        authors_raw = pub.get('bib', {}).get('author', 'Unknown Authors')
        year = pub.get('bib', {}).get('year', None)
        publication = pub.get('bib', {}).get('venue', 'N/A')  # Venue name
        cited_by = pub.get('num_citations', 0)
        tags = pub.get('bib', {}).get('keywords', '').split(",")  # Optional tags
        link = pub.get('pub_url', '')

        # Check and use another valid field (e.g., date, publication year) for the date field
        publication_date = pub.get('bib', {}).get('pub_date', None)  # Trying to get a valid date
        if not publication_date:
            if not year or not year.isdigit():  # Handle missing or invalid year
                year = "2000"  # Default year
            formatted_date = f"{year}-01-01"
        else:
            # Use the `pub_date` as the fallback date if available
            formatted_date = publication_date if publication_date else "2000-01-01"

        # Skip duplicates and unmatched authors
        if title in processed_titles:
            continue
        if not author_matches(authors_raw, known_authors):
            print(f"Skipping '{title}' - Authors do not match known authors.")
            continue

        # Categorize based on CrossRef and fallback
        publication_type_numeric, publication_type_label = categorize_paper(publication, title)

        # Prepare file path
        safe_title = clean_file_name(title)
        folder_path = os.path.join(author_folder, safe_title)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, "index.md")

        # Write content
        paper_data = f"""---
title: "{title}"

# Authors
authors:
  - {", ".join(f'"{author.strip()}"' for author in authors_raw.split(","))}

# Date of publication
date: {formatted_date}

# Publication type
publication_types: ["{publication_type_numeric}"]  # {publication_type_label}

# Publication name and details
publication: "{publication}"
cited_by: "{cited_by}"

# Tags for categorization
tags:
  - {", ".join(f'"{tag.strip()}"' for tag in tags)}

# Links to resources
url_pdf: "{link}"  # Link to the resource
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""

# Featured image (optional)
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated projects (optional)
projects: []

# Slides (optional)
slides: ""
---
"""

        with open(file_path, "w") as f:
            f.write(paper_data)

        processed_titles.add(title)
        print(f"Saved: {file_path}")

print("All publications have been organized into folders by author.")
