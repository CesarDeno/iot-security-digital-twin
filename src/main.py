import sys
import asyncio
import logging
from contextlib import asynccontextmanager
from database import test_connection

# --- FIX WINDOWS ---
if sys.platform.startswith("win"):
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    except Exception:
        pass

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mqtt_handler import mqtt
from config import MQTT_BROKER

# Configuración de Logs
logger = logging.getLogger("uvicorn.info")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Iniciar conexión MQTT explícitamente
    logger.info("[BROKER] Iniciando cliente MQTT...")
    await mqtt.mqtt_startup()
    
    # 2. Verificar base de datos
    logger.info("[MONGO] Verificando conexión a MongoDB...")
    await test_connection()
    
    logger.info("✅ [SISTEMA] Esperando mensajes...")
    yield
    
    # 3. Cerrar conexión al apagar
    await mqtt.mqtt_shutdown()

app = FastAPI(title="Middleware IoT: MQTT + Mongo", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "System Online", 
        "mode": "MQTT Listener",
        "broker": MQTT_BROKER
    }