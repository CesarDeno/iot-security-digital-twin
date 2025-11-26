import asyncio
import json
import random
import os
import uuid
from gmqtt import Client as MQTTClient
from dotenv import load_dotenv
from datetime import datetime

# Cargar config
load_dotenv()
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
TOPIC_TELEMETRY = os.getenv("TOPIC_TELEMETRY", "iot/telemetry")
TOPIC_COMMANDS = os.getenv("TOPIC_COMMANDS", "iot/commands")

STOP = asyncio.Event()
CLIENT_ID = f"mock_sec_{uuid.uuid4().hex[:6]}"

def on_connect(client, flags, rc, properties):
    print(f"✅ [SECURITY DEVICE] Conectado como: {CLIENT_ID}")
    client.subscribe(TOPIC_COMMANDS)

def on_message(client, topic, payload, qos, properties):
    print(f"⚡ [COMANDO RECIBIDO]: {payload.decode()}")

def on_disconnect(client, packet, exc=None):
    print("⚠️ [DESCONECTADO] Conexión perdida con el Broker.")

async def main():
    client = MQTTClient(CLIENT_ID)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    door_is_open = False

    while not STOP.is_set():
        try:
            await client.connect(MQTT_BROKER)
            
            while not STOP.is_set():
                # --- Lógica de Simulación Mejorada ---
                
                # Probabilidad de intento fallido (ej. tarjeta inválida)
                is_access_granted = random.random() > 0.1 # 90% éxito, 10% fallo

                if not is_access_granted:
                    # Intento fallido: La puerta NO cambia de estado, pero se registra el evento
                    new_status = "CLOSED" 
                    method = random.choice(["rfid", "password", "remote"])
                    print(f"❌ ACCESO DENEGADO ({method})")
                
                elif door_is_open:
                    new_status = "CLOSED"
                    method = None
                    door_is_open = False
                    is_access_granted = True # Cerrar siempre es autorizado
                    print("🔒 Puerta CERRADA")
                else:
                    new_status = "OPENED"
                    method = random.choice(["rfid", "password", "remote"])
                    door_is_open = True
                    is_access_granted = True
                    print(f"🔓 Puerta ABIERTA usando {method}")

                data = {
                    "device_id": "access_control_01",
                    "door_status": new_status,
                    "access_method": method,
                    "access_granted": is_access_granted,
                    "timestamp": datetime.now().isoformat()
                }
                
                if client.is_connected:
                    client.publish(TOPIC_TELEMETRY, json.dumps(data), qos=0)
                else:
                    print("⏳ Esperando reconexión...")
                    break 

                await asyncio.sleep(random.randint(3, 8))

        except Exception as e:
            print(f"🔄 Reintentando conexión en 3s...")
            await asyncio.sleep(3)
        finally:
            if hasattr(client, 'is_connected') and client.is_connected:
                try:
                    await client.disconnect()
                except Exception:
                    pass

if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Simulador detenido.")