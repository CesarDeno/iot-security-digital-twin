# Proyecto Final Integrador: Sistema Ciberfísico y Gemelo Digital

Middleware IoT desarrollado en **Python (FastAPI)** que conecta un **prototipo físico (ESP32)** con un **Gemelo Digital en Unity**, utilizando **MQTT** para transmisión en tiempo real y **MongoDB** para almacenamiento histórico.

## 🚀 Instrucciones de Instalación y Ejecución

### 1. Configuración del Entorno Python

```
python -m venv .venv
.venv\Scripts\activate
```

### 2. Infraestructura (Docker)

```
docker-compose up -d
```

### 3. Instalación de Dependencias

```
pip install -r requirements.txt
```

### 4. Ejecución del Middleware

```
cd src
python run.py
```

## 🧪 Herramientas de Simulación (Testing)

### Simulador de Hardware (Mock ESP32)

```
python mock_esp32.py
```

### Visor Web (Mock Unity)

Abrir `mock/mock_unity.html`.

## 🔑 Credenciales y Puertos

| Servicio   | Host      | Puerto | Usuario   | Contraseña |
| ---------- | --------- | ------ | --------- | ---------- |
| MongoDB    | localhost | 27017  | iot_admin | 940194     |
| MQTT (TCP) | localhost | 1883   | (Anónimo) | -          |
| MQTT (WS)  | localhost | 9001   | (Anónimo) | -          |
| API REST   | localhost | 8000   | -         | -          |

MongoDB Compass URI:

```
mongodb://iot_admin:940194@localhost:27017/?authSource=admin
```
