import json
import logging
from datetime import datetime
from fastapi_mqtt import FastMQTT, MQTTConfig
from config import MQTT_BROKER, MQTT_PORT, TOPIC_TELEMETRY, TOPIC_COMMANDS
from database import save_sensor_data

# Configuración de Logs
logger = logging.getLogger("uvicorn.info")

# 1. Configuración
mqtt_config = MQTTConfig(
    host=MQTT_BROKER,
    port=MQTT_PORT,
    keepalive=60
)

# 2. Instancia del cliente
mqtt = FastMQTT(config=mqtt_config)

# 3. Función CONNECT (Se ejecuta sola al conectarse)
@mqtt.on_connect()
def connect(client, flags, rc, properties):
    logger.info(f"✅ [BROKER] Python conectado al Broker MQTT: {MQTT_BROKER}")

    
    # Suscribirse aquí para no perder la suscripción si se reconecta
    mqtt.client.subscribe(TOPIC_TELEMETRY, qos=0)
    logger.info(f"✅ [BROKER] Escuchando TOPIC: {TOPIC_TELEMETRY}")

# 4. Función MESSAGE (Se ejecuta sola al recibir datos)
@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    if topic == TOPIC_TELEMETRY:
        try:
            payload_str = payload.decode()
            logger.info(f"[MQTT HANDLER] Recibido: {payload_str}")
            
            data_json = json.loads(payload_str)
            
            if not data_json.get("timestamp"):
                data_json["timestamp"] = datetime.now().isoformat() 

            await save_sensor_data(data_json)

        except Exception as e:
            logger.info(f"❌ [BROKER]  Error procesando mensaje MQTT: {e}")
    else:
        logger.info(f"❌ [BROKER] Tema desconocido: {topic}")