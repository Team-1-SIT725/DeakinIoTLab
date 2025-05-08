---
title: Teacher-Student Network for RF Sensing
date: 2025-05-08
type: landing

sections:
  - block: markdown
    design:
      columns: "1"
      background: 
        color: "#ffffff"
      spacing:
        padding: ["60px", "0", "60px", "0"]
      css_class: fullscreen
    content:
      title: Teacher-Student Network Architecture
      subtitle: Enhancing RF posture detection through multi-modal knowledge transfer
      text: |
        Our **Teacher-Student Network** is a key component of the **Deakin RF-Sensing framework**, where we harness the power of **multi-modal learning** to teach RF-based systems how to interpret human posture — using visual guidance from camera data.

        This architecture empowers our models to learn complex spatial patterns from rich visual features and apply them to minimal RF input.

        ---

        ### 🧠 How It Works

        **1. Vision-Based Teacher Network**  
        🎥 A high-accuracy pose estimation model processes video frames to serve as the "teacher" — generating supervision signals like keypoint heatmaps and pose vectors.

        **2. RF-Based Student Network**  
        📡 A lightweight neural network learns to mimic the outputs of the teacher model using only RF signal features — enabling camera-free inference.

        **3. Correlated Knowledge Distillation (CKD)**  
        🔗 A unique training pipeline that aligns temporal and spatial representations between the two networks, improving the student’s understanding of motion and posture.

        **4. Shared Temporal Encoding**  
        ⏱️ Both networks use time-series encoders to preserve the dynamics of human motion and boost temporal awareness.

        **5. Post-Training Deployment on Edge**  
        💻 Once trained, the student model can operate independently on SDR edge devices in real-world environments.

        ---

        ### 🚀 Research Outcomes

        - Reduced model size by 80% with minimal loss in accuracy
        - Achieved privacy-preserving pose detection in environments unsuitable for cameras
        - Published architecture in top-tier sensor and AI conferences

        ---

        The Teacher-Student Network enables us to combine the richness of vision with the practicality of RF — creating **smart, secure, and scalable human monitoring systems**.
---
