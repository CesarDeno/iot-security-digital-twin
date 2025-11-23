import os
from pathlib import Path
from dotenv import load_dotenv

# --- AJUSTE DE RUTAS ---
# src/config.py -> sube 2 niveles -> raiz/.env
base_path = Path(__file__).resolve().parent.parent
env_path = base_path / ".env"

# Cargar variables
load_dotenv(dotenv_path=env_path)

# --- CONFIGURACIÓN (Con valores por defecto para seguridad) ---
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017") 
DB_NAME = os.getenv("MONGO_DB_NAME", "iot_project")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", "sensor_data")

# MQTT
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883)) 
TOPIC_TELEMETRY = os.getenv("TOPIC_TELEMETRY", "iot/telemetry")
TOPIC_COMMANDS = os.getenv("TOPIC_COMMANDS", "iot/commands")