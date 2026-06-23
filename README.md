# PPEGuard-YOLOv5
# 🦺 Real-Time Safety Equipment Detection using YOLOv5

## Overview

This project is a real-time Personal Protective Equipment (PPE) detection system built using YOLOv5 and PyTorch. It monitors live camera feeds and identifies safety compliance violations, such as workers not wearing hard hats, face masks, or safety vests.

The system is designed to improve workplace safety by providing automated monitoring and real-time detection capabilities. It also incorporates containerization and logging practices commonly used in DevOps environments for scalable and repeatable deployments.

---

## Features

* Real-time PPE detection from webcam or live video streams
* Detects:

  * Hard Hats
  * Face Masks
  * Safety Vests
* Identifies missing safety equipment and flags violations
* High-speed object detection using YOLOv5
* Dockerized deployment for environment consistency
* Structured logging for monitoring and incident tracking
* Easy integration with monitoring and observability pipelines

---

## Tech Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Core Development               |
| PyTorch          | Deep Learning Framework        |
| YOLOv5           | Object Detection Model         |
| OpenCV           | Video Capture & Processing     |
| Docker           | Containerization               |
| Webcam Streaming | Real-Time Video Input          |
| Logging          | Monitoring & Incident Tracking |

---

## System Architecture

```text
Webcam Feed
      │
      ▼
YOLOv5 Detection Engine
      │
      ▼
PPE Detection & Violation Analysis
      │
      ├── Safety Compliant
      │
      └── PPE Violation Detected
                 │
                 ▼
         Structured Log Generation
                 │
                 ▼
      Monitoring / Observability Pipeline
```

---

## Project Objectives

* Improve workplace safety through automated monitoring.
* Detect PPE violations in real time.
* Provide scalable deployment using Docker containers.
* Generate logs for auditing, monitoring, and incident response workflows.
* Demonstrate the integration of AI and DevOps practices in industrial safety systems.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/real-time-safety-equipment-detection.git

cd real-time-safety-equipment-detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Using Python

```bash
python detect.py
```

The webcam feed will open and begin detecting PPE compliance in real time.

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t ppe-detector .
```

### Run Container

```bash
docker run ppe-detector
```

This ensures consistent deployment across development, testing, and production environments.

---

## Logging & Monitoring

The application generates structured logs containing:

* Detection timestamp
* Detected PPE classes
* Confidence scores
* Violation events
* Camera source information

These logs can be forwarded to centralized monitoring platforms for:

* Incident response
* Safety audits
* Compliance tracking
* Operational monitoring

---

## Sample Use Cases

* Construction Site Monitoring
* Manufacturing Plants
* Industrial Safety Compliance
* Warehouse Operations
* Mining and Heavy Equipment Environments

---

## Future Enhancements

* Email/SMS alerts for PPE violations
* Dashboard for live monitoring
* Multi-camera support
* Cloud deployment using Kubernetes
* Integration with ELK Stack and Prometheus/Grafana
* Historical analytics and reporting

---

## Learning Outcomes

Through this project, the following concepts were applied:

* Deep Learning-Based Object Detection
* YOLOv5 Model Training and Inference
* Computer Vision Applications
* Real-Time Video Processing
* Docker Containerization
* Logging and Observability
* DevOps Deployment Practices

---

## Author

**Praba L K**

Software Engineer | Cloud & DevOps Enthusiast | AI/ML Practitioner

LinkedIn: Add your profile link here

GitHub: Add your GitHub profile link here

