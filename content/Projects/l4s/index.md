---
title: Experience-Driven L4S Internet Service Architecture in FreeBSD

summary: A research project enhancing low-latency, lossless, and scalable internet service delivery using the FreeBSD networking stack.

abstract: |
  This project, supported by the APNIC Foundation, focuses on implementing the IETF-defined L4S (Low Latency, Low Loss, Scalable Throughput) architecture within the FreeBSD kernel to support real-time, congestion-aware internet applications. The work involves modifying queue management systems and using reinforcement learning to dynamically optimize performance for modern digital services including cloud gaming, real-time video, and industrial IoT.

date: 2025-05-12

featured: true

image:
  caption: 'Implementation of L4S in FreeBSD for next-generation low-latency networking.'
  focal_point: Right
  filename: l4s-networking.jpg

projects: []

tags: ["L4S", "FreeBSD", "Internet Architecture", "Networking", "QoS", "QoE"]

url_pdf: ""
url_slides: ""
url_code: ""
url_video: ""
external_link: "https://apnic.foundation/projects/implementing-an-experience-driven-l4s-internet-service-architecture-in-freebsd/"
---

## Implementing an Experience-driven Low Latency, Low Loss, and Scalable Throughput (L4S) Internet Service Architecture using FreeBSD

**A research initiative by Deakin University's IoT & Software Engineering Lab, supported by the APNIC Foundation**

---

### Project Overview

This project explores the integration of Deep Reinforcement Learning (DRL) and Large Language Models (LLMs) with the Low Latency, Low Loss, and Scalable Throughput (L4S) architecture to improve Internet congestion control. Hosted at Deakin University and funded by the APNIC Foundation, the project implements modular congestion control algorithms within FreeBSD, evaluates them on custom-built testbeds, and disseminates experimental results, software and datasets to the wider community.

---

### Key Outcomes

- DRL-based Multipath TCP (MPTCP) and AQM modules implemented in FreeBSD  
- Public testbed infrastructure available for reproducible experimentation  
- Peer-reviewed publications and ongoing contributions in academic/industry conferences  
- Student internships, mentoring, and curriculum integration for skill development  
- Ongoing industry and research partnerships  

---

### Open Source Software and Datasets

All source code and supporting data from this project have been made openly available to support reproducibility and collaboration:

- Experimental L4S testbed setup: [FreeBSD-L4S-Experiments](https://github.com/MPTCP-FreeBSD/FreeBSD-L4S-Experiments)  
- DRL-enhanced congestion control stack for FreeBSD: [FreeBSD-DRL-L4S](https://github.com/MPTCP-FreeBSD/FreeBSD-DRL-L4S)  
- Predictive congestion marking using LLMs: [L4S-LLM](https://github.com/MPTCP-FreeBSD/L4S-LLM)  
- Adaptive TCP fairness via fine-tuned LLMs: [LLM-TCP](https://github.com/MPTCP-FreeBSD/LLM-TCP)  
- AQM decision models powered by LLM-based inference: [AQM-LLM](https://github.com/MPTCP-FreeBSD/AQM-LLM)  

---

### Publications

- **Pokhrel et al.**, “DDPG-MPCC: An experience driven multipath performance oriented congestion control,” *Future Internet*, Feb. 2024. [DOI](https://doi.org/10.3390/fi16020037)  
- **Shrestha et al.**, “On the fairness of Internet congestion control over WiFi with deep reinforcement learning,” *Future Internet*, Sept. 2024. [DOI](https://doi.org/10.3390/fi16090330)  
- **Satish et al.**, “AQM in L4S with A3C: A FreeBSD networking stack perspective,” *Future Internet*, Aug. 2024. [DOI](https://doi.org/10.3390/fi16080265)  
- **Pokhrel et al.**, “Multipath TCP implementation under FreeBSD-13 for pluggable ML models,” *Computer Networks*, 2024. [DOI](https://doi.org/10.1016/j.comnet.2024.110671)  
- **Shrestha et al.**, “Adapting LLMs for improving TCP fairness over WiFi,” *arXiv*, Dec. 2024. [arXiv:2412.18200](https://arxiv.org/abs/2412.18200)  
- **Satish et al.**, “Distilling LLMs for network AQM,” *arXiv*, Jan. 2025. [arXiv:2501.16734](https://arxiv.org/abs/2501.16734)  

---

### Get Involved

Interested in collaborating or learning more? Our project continues to grow through academic and industry partnerships, conference engagement, and educational outreach.

**Contact:** [jonathan.kua@deakin.edu.au](mailto:jonathan.kua@deakin.edu.au)