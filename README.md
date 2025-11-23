# Final Integrative Project: Cyber-Physical System and Digital Twin

IoT middleware developed in **Python (FastAPI)** that connects a **physical prototype (ESP32)** with a **Digital Twin in Unity**, using **MQTT**  for real-time
transmission and **MongoDB** for historical storage.

## 🚀 Installation and Execution Instructions

### 1. Python Environment Setup

```
python -m venv .venv
.venv\Scripts\activate
```

### 2. Infrastructure (Docker)

```
docker-compose up -d
```

### 3. Dependency Installation

```
pip install -r requirements.txt
```

### 4.Middleware Execution

```
cd src
python run.py
```

## 🧪 Simulation Tools (Testing)

### Hardware Simulator (Mock ESP32)

```
python mock/mock_esp32.py
```

### Web Viewer (Mock Unity)

Open `mock/mock_unity.html`.

## 🔑 Credentials and Ports

| Service    | Host      | Port   | User      | Password   |
| ---------- | --------- | ------ | --------- | ---------- |
| MongoDB    | localhost | 27017  | iot_admin | 940194     |
| MQTT (TCP) | localhost | 1883   | (Anónimo) | -          |
| MQTT (WS)  | localhost | 9001   | (Anónimo) | -          |
| API REST   | localhost | 8000   | -         | -          |

MongoDB Compass URI:

```
mongodb://iot_admin:940194@localhost:27017/?authSource=admin
```
