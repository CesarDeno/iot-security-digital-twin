from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from mqtt_handler import mqtt, TOPIC_COMMANDS
from websocket_manager import manager
from config import MQTT_BROKER

app = FastAPI(title="Middleware IoT: MQTT + Unity")

# --- FIX: Permitir conexiones desde cualquier origen (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las conexiones
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar MQTT con la app
mqtt.init_app(app)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Endpoint WebSocket para Unity.
    Maneja la conexión y reenvía comandos hacia MQTT.
    """
    await manager.connect(websocket)
    try:
        while True:
            # Recibir comando de Unity (ej: {"action": "led_on"})
            data = await websocket.receive_text()
            print(f"🎮 Comando de Unity: {data}")
            
            # Publicar en MQTT hacia el ESP32
            mqtt.publish(TOPIC_COMMANDS, data) 
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/")
async def root():
    return {"status": "System Online", "broker": MQTT_BROKER}