# XIS Django FullStack Integration (July 2026 Internship)

## Project Overview

This project integrates an AI image classification model into a Django Full-Stack application. The system exposes AI inference through REST APIs, WebSockets, and MQTT communication while providing centralized logging and error handling.

The application performs image classification using an ONNX model and demonstrates an end-to-end communication pipeline suitable for real-time AI applications.

---

# Features

- Django REST Framework APIs
- ONNX Runtime AI Inference
- Image Classification
- WebSocket Communication (Django Channels)
- MQTT Publish/Subscribe Messaging
- Shared Inference Engine
- Centralized Logging
- Error Handling
- Performance Measurement
- End-to-End Communication Pipeline

---

# Project Structure

```
XIS_Django_FullStack_Integration_2026-07_INT/

│
├── backend/
│   ├── config/
│   ├── inference/
│   │   ├── api/
│   │   ├── mqtt/
│   │   ├── services/
│   │   ├── utils/
│   │   └── websocket/
│   ├── manage.py
│   └── test_mqtt.py
│
├── input/
│
├── models/
│   ├── convnextv2.onnx
│   └── convnextv2.onnx.data
│
├── results/
│   ├── logs/
│   ├── mqtt/
│   ├── rest_api/
│   └── websocket/
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python 3.13
- Django
- Django REST Framework
- Django Channels
- Daphne
- ONNX Runtime
- OpenCV
- NumPy
- MQTT (Paho MQTT)
- Git
- Git LFS

---

# Model

Model Type

- ConvNeXt V2

Framework

- ONNX Runtime

Classes

- Buildings
- Forest
- Glacier
- Mountain
- Sea
- Street

---

# REST API Endpoints

## Health Check

```
GET /api/health/
```

Returns application health status.

---

## Model Information

```
GET /api/model-info/
```

Returns loaded model information including:

- Model Name
- Execution Provider
- Input Layer
- Output Layer

---

## Image Inference

```
POST /api/inference/
```

Upload an image using multipart/form-data.

Response:

```json
{
    "status": "success",
    "prediction": "forest",
    "confidence": 99.98,
    "processing_time_ms": 24.56,
    "model": "convnextv2.onnx"
}
```

---

# WebSocket

Endpoint

```
ws://127.0.0.1:8000/ws/inference/
```

Features

- Client Connection
- JSON Messaging
- Real-Time Communication
- Logging

---

# MQTT

Broker

```
broker.emqx.io
```

Topic

```
xis/inference/results
```

Features

- Publish Prediction Results
- Subscribe to Prediction Messages
- Real-Time Messaging

---

# Logging

Application logs are stored in:

```
results/logs/application.log
```

Logged Events

- REST API Requests
- Predictions
- MQTT Events
- WebSocket Events
- Exceptions
- Processing Information

---

# Installation

Clone repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

Navigate to backend

```bash
cd backend
```

Run server

```bash
python manage.py runserver
```

Application runs at

```
http://127.0.0.1:8000/
```

---

# Testing

REST API

Tested using Postman

- Health API
- Model Info API
- Image Inference API

WebSocket

Tested using Postman WebSocket Client.

MQTT

Tested using publish/subscribe communication with EMQX public broker.

---

# Results

The project successfully demonstrates:

- AI image classification using ONNX Runtime
- REST API inference
- Real-time WebSocket communication
- MQTT publish/subscribe messaging
- Centralized logging
- End-to-end integration

---

# Future Improvements

- Live camera streaming
- WebSocket image inference
- User authentication
- Docker deployment
- Redis-backed channel layer
- Production MQTT broker
- GPU deployment
- Frontend dashboard

---
