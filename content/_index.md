---
title: IoT & Software Engineering Lab
date: 2022-10-24
type: landing

sections:

  - block: hero
    content:
      title: |
        Deakin University IoT and Software Engineering Lab
      text: |
        <br>
        The Deakin IoT Lab drives innovation at the intersection of connected devices and intelligent systems. Our work spans Internet of Things (IoT), software engineering, and data-driven solutions aimed at creating real-world impact across health, environment, manufacturing, and smart cities.
      image:
        filename: welcome.jpg
        alt: Research overview image
        placement: right
        style: |
          animation: fadeIn 2s ease-in-out;
    design:
      align: center
      font_size: '34px'
      color: '#222'
      css_class: fade-in-section

  - block: markdown
    content:
      title: About the Lab
      text: |
        The IoT and Software Engineering Lab at Deakin University is a hub for research, prototyping, and innovation. Our mission is to solve real-world challenges using connected systems, scalable software architectures, and intelligent sensing technologies.

        We focus on key areas such as:
        - Embedde and real-time systems
        - Wireless sensor networks
        - Edge and cloud computing integration
        - Smart infrastructure and energy systems
        - Privacy-preserving IoT architectures

        Our team works closely with academic collaborators, industry partners, and government bodies to deliver translational outcomes and student-led innovations that are future-ready.
    design:
      columns: '1'
      spacing:
        padding: ['40px', '0', '40px', '0']
      css_class: fade-in-section

  - block: collection
    content:
      title: Recent Publications
      text: Explore our latest peer-reviewed research contributions in IoT, edge computing, smart systems, and intelligent data pipelines.
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'
      css_class: fade-in-section

custom_css:
  - css/animations.css
---