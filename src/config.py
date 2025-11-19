import os
from pathlib import Path
from dotenv import load_dotenv

base_path = Path(__file__).resolve().parent.parent
env_path = base_path / ".env"

# Cargar variables desde el archivo .env
load_dotenv(dotenv_path=env_path)

# --- CONFIGURACIÓN ---
MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("MONGO_DB_NAME")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

# Configuración MQTT
MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
TOPIC_TELEMETRY = os.getenv("TOPIC_TELEMETRY")
TOPIC_COMMANDS = os.getenv("TOPIC_COMMANDS")