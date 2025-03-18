---
title:
  
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Deakin University
        Internet of Things (IoT) Lab
      image:
        filename: welcome.jpg
      text: |
        <br>
        The **Deakin IoT Lab** is at the forefront of innovation, teaching, and research in the Internet of Things (IoT), driving solutions that shape the future of smart technologies and connected systems.

  - block: collection
    content:
      title: Latest News
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: news 
    design:
      view: card
      columns: '1'

  - block: markdown
    content:
      title: Our Vision in IoT
      text: |
        The Deakin IoT Lab is committed to advancing IoT technology through research, collaboration, and real-world applications.
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest IoT Research
      text: "Explore groundbreaking research from Deakin University on IoT technologies."
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article' 
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title: Learn More About IoT at Deakin
      text: |
        {{% cta cta_link="https://futured.deakin.edu.au/concepts/internet-of-things/" cta_text="Explore More →" %}}
    design:
      columns: '1'
      background:
        image:
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
        # Add a semi-transparent background color for the text area
        background_color: rgba(0, 0, 0, 0.4)  # Adjust the alpha value for transparency (0.0 is fully transparent, 1.0 is fully opaque)
        text_color_light: true  # Ensure text color is light for better contrast
        text_align: right  # Adjust text position, options: 'left', 'center', 'right'
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen-overlay
---