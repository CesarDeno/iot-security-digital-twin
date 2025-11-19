# Proyecto Final Integrador: Sistema Ciberfísico y Gemelo Digital

Middleware IoT desarrollado en **Python (FastAPI)** que conecta un
prototipo físico (**ESP32**) con un **Gemelo Digital en Unity**,
utilizando **MQTT** para transmisión en tiempo real y **MongoDB** para
almacenamiento histórico.

------------------------------------------------------------------------

## 🚀 Instrucciones de Instalación y Ejecución

### 1. Configuración del Entorno Python

``` bash
python -m venv .venv
```

``` bash
.venv\Scripts\activate
```

### 2. Infraestructura (Docker)

``` bash
docker-compose up -d
```

### 3. Instalación de Dependencias

``` bash
pip install -r requirements.txt
```

### 4. Ejecución del Middleware

``` bash
cd src
uvicorn main:app --reload 
```

------------------------------------------------------------------------

## 🔗 Enlaces Útiles

-   API Server: http://127.0.0.1:8000
-   Swagger: http://127.0.0.1:8000/docs
-   MongoDB Local: mongodb://localhost:27017
-   Broker MQTT: tcp://localhost:1883
