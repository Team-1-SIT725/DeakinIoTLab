---
title: Publications

# Description for the Publications page
description: >
  Explore the latest research contributions from our team, categorized into journal articles, conference papers, and preprints. Dive into groundbreaking research on topics like IoT, AI, Blockchain, and 6G.

sections:
  # Journal Articles Section
  - title: Journal Articles
    description: >
      Peer-reviewed journal publications featuring advanced research findings in IoT, Federated Learning, and more.
    link: /publication/journal-article/
    design:
      columns: '1'
      css_class: publication-section

  # Conference Papers Section
  - title: Conference Papers
    description: >
      Contributions presented at international conferences, showcasing innovative approaches in mobile computing, AI, and networking.
    link: /publication/conference-paper/
    design:
      columns: '1'
      css_class: publication-section

  # Preprints Section
  - title: Preprints
    description: >
      Early-stage research shared on open-access platforms, offering a glimpse into the latest breakthroughs before formal publication.
    link: /publication/preprint/
    design:
      columns: '1'
      css_class: publication-section

  # Recent Publications Section
  - title: Recent Publications
    description: >
      Here are some of our recent publications in the areas of IoT, AI, and networking:
    publications:
      - title: "Active Queue Management in L4S with Asynchronous Advantage Actor-Critic: A FreeBSD Networking Stack Perspective"
        authors: "Deol Satish, Jonathan Kua, Shiva Pokhrel"
        date: "2000-01-01"
        publication_types: ["2"]  # '1' = Conference Paper, '2' = Journal Article, '3' = Preprint
        url_pdf: "https://dro.deakin.edu.au/articles/journal_contribution/Active_Queue_Management_in_L4S_with_Asynchronous_Advantage_Actor-Critic_A_FreeBSD_Networking_Stack_Perspective/26762443"
        design:
          css_class: publication-card

      - title: "Another Example Journal Article"
        authors: "Example Author"
        date: "2021-05-12"
        publication_types: ["2"]
        url_pdf: "https://example.com/another-article"
        design:
          css_class: publication-card

      - title: "Preprint on IoT Technology"
        authors: "Author Name"
        date: "2023-09-10"
        publication_types: ["3"]
        url_pdf: "https://example.com/iot-preprint"
        design:
          css_class: publication-card

    design:
      columns: '1'
      background:
        image: 
          filename: publications-bg.jpg
          filters:
            brightness: 0.6
          position: center
          size: cover
      spacing:
        padding: ['20px', '30px', '20px', '30px']
      css_class: fullscreen
      margin: 50px
---
