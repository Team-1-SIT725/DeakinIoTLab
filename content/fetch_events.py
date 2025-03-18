import requests
import os
import re
import yaml

EVENTS_API_KEY = "aea1bba28a83406084929c7d5fbc565f"  # Use the appropriate API key for fetching events

def sanitize_filename(title):
    """Sanitize the title to create a valid filename."""
    sanitized_title = re.sub(r'[^\w\s-]', '', title)  # Remove special characters
    sanitized_title = sanitized_title.replace(" ", "-").lower()
    return sanitized_title

def download_image(image_url, save_path):
    """Download and save the image locally, ensuring the directory exists."""
    if not image_url:
        return None  # Skip if no image

    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure directory exists

    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return save_path
    except Exception as e:
        print(f"❌ Failed to download image: {e}")
    
    return None

def fetch_victoria_events():
    """Fetch events related to Victoria, Australia."""
    url = f"https://api.example.com/events?location=Victoria&apiKey={EVENTS_API_KEY}"  # Replace with actual events API
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch events. Status Code: {response.status_code} | Response: {response.text}")
        return []

    events = response.json().get("events", [])[:5]  # Limit to 5 events
    event_list = []

    for event in events:
        event_data = {
            "title": event["name"],  # Assuming the event has a "name" field
            "url": event["url"],  # Assuming the event has a "url" field
            "summary": event["description"],  # Assuming the event has a "description" field
            "image": event.get("image", ""),  # Assuming the event has an "image" field
            "date": event["date"],  # Assuming the event has a "date" field
            "location": event["location"],  # Assuming the event has a "location" field
        }
        event_list.append(event_data)
        save_event_as_markdown(event_data)

    return event_list

def save_event_as_markdown(event):
    """Save each event as a markdown file in the proper directory."""
    file_title = sanitize_filename(event['title'])
    filename = f"content/events/{file_title}/index.md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    os.makedirs("static/event_images", exist_ok=True)  # ✅ Ensure image directory exists

    # Download image and save it locally
    image_filename = sanitize_filename(event["title"]) + ".jpg"
    image_path = f"static/event_images/{image_filename}"
    downloaded_image_path = download_image(event["image"], image_path)

    content_dict = {
        "title": event["title"],
        "date": event["date"],
        "summary": event["summary"],
        "external_link": event["url"],  # ✅ Use `external_link` instead of `news_url`
        "location": event["location"],
        "image": {"filename": f"event_images/{image_filename}" if downloaded_image_path else ""},
    }

    yaml_content = yaml.dump(content_dict, default_flow_style=False, allow_unicode=True)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"---\n{yaml_content}---\n")

    print(f"✅ Created: {filename}")

if __name__ == "__main__":
    fetch_victoria_events()
    print("🎉 Events updated successfully!")
