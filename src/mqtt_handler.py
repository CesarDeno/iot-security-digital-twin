import json
from datetime import datetime
from fastapi_mqtt import FastMQTT, MQTTConfig
from config import MQTT_BROKER, MQTT_PORT, TOPIC_TELEMETRY, TOPIC_COMMANDS
from database import save_sensor_data
from websocket_manager import manager

# Configuración del cliente MQTT
mqtt_config = MQTTConfig(
    host=MQTT_BROKER,
    port=MQTT_PORT,
    keepalive=60
)

mqtt = FastMQTT(config=mqtt_config)

@mqtt.on_connect()
def connect(client, flags, rc, properties):
    print(f"📡 Conectado al Broker MQTT: {MQTT_BROKER}")
    mqtt.client.subscribe(TOPIC_TELEMETRY)
    print(f"👂 Escuchando tema: {TOPIC_TELEMETRY}")

@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    try:
        payload_str = payload.decode()
        print(f"📥 Recibido MQTT [{topic}]: {payload_str}")
        
        data_json = json.loads(payload_str)
        
        # 1. Añadir timestamp si falta
        if "timestamp" not in data_json:
            data_json["timestamp"] = datetime.now()

        # 2. Guardar en BD (usando la función auxiliar)
        await save_sensor_data(data_json)

        # 3. Enviar a Unity
        msg_to_unity = {
            "type": "sensor_update",
            "payload": data_json
        }
        await manager.broadcast(msg_to_unity)

    except Exception as e:
        print(f"Error procesando mensaje MQTT: {e}")