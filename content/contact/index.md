---
title: Contact
date: 2022-10-24

type: landing

sections:
  - block: contact
    content:
      title: Contact
      text: |-
        Get in touch with the Deakin IoT Research Group for inquiries about our projects, research opportunities, or collaborations.
      email: iotlab@deakin.edu.au
      phone: +61 3 5227 1100
      address:
        street: 75 Pigdons Road
        city: Waurn Ponds
        region: VIC
        postcode: '3216'
        country: Australia
        country_code: AU
      coordinates:
        latitude: '-38.1984'
        longitude: '144.2965'
      directions: Visit the Deakin University Waurn Ponds Campus. Find the IoT Lab in Building KA, Level 2, Room 205.
      office_hours:
        - 'Monday to Friday: 09:00 to 17:00'
      appointment_url: ''
    
      # Automatically link email and phone or display as text?
      autolink: true
    
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '1'

  - block: markdown
    content:
      title: Visit Us
      subtitle: ''
      text: |
        Learn more about our research and projects at the [Deakin IoT Research Group](https://www.deakin.edu.au/iot-lab).
    design:
      columns: '1'
      background:
        image: 
          filename: contact.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen
---
