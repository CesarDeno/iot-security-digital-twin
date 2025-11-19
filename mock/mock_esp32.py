import asyncio
import json
import random
import os
import uuid
from pathlib import Path
from gmqtt import Client as MQTTClient
from dotenv import load_dotenv
from datetime import datetime

base_path = Path(__file__).resolve().parent.parent
env_path = base_path / ".env"

# Cargar variables desde el archivo .env
load_dotenv(dotenv_path=env_path)

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
    print(f"⚠️ [DESCONECTADO] ({exc})")

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
                # Lógica de simulación
                if door_is_open:
                    new_status = "CLOSED"
                    method = None
                    door_is_open = False
                    print("🔒 Puerta CERRADA")
                else:
                    new_status = "OPEN"
                    method = random.choice(["NFC", "KEYPAD"])
                    door_is_open = True
                    print(f"🔓 Puerta ABIERTA usando {method}")

                data = {
                    "device_id": "access_control_01",
                    "door_status": new_status,
                    "access_method": method,
                    "timestamp": datetime.now().isoformat()
                }
                
                # --- FIX: Verificar conexión antes de publicar ---
                if client.is_connected:
                    try:
                        client.publish(TOPIC_TELEMETRY, json.dumps(data), qos=0)
                    except OSError:
                        print("⚠️ Fallo al publicar (Socket cerrado), reconectando...")
                        break # Rompe el bucle interno para reconectar
                else:
                    print("⏳ Esperando conexión para publicar...")
                    break

                await asyncio.sleep(random.randint(3, 8))

        except Exception as e:
            print(f"❌ Error de conexión o Broker caído. Reintentando en 3s...")
            await asyncio.sleep(3)
        finally:
            # Limpieza segura
            if client.is_connected:
                try:
                    await client.disconnect()
                except:
                    pass

if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Detenido.")