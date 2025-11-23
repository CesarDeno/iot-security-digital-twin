from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL, DB_NAME, COLLECTION_NAME
import logging
import asyncio

# Configuración de Logs
logger = logging.getLogger("uvicorn.info")

# Inicialización del cliente
client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

async def save_sensor_data(data: dict):
    """Guarda los datos del sensor en MongoDB con log de depuración"""
    try:
        result = await collection.insert_one(data)
        #logger.info(f"✅ [MONGODB] Guardado OK. ID: {result.inserted_id}")
    except Exception as e:
        logger.info(f"❌ [MONGODB] No se pudo guardar: {e}")

async def test_connection():
    """Prueba rápida de conexión al iniciar la app"""
    try:
        await client.admin.command('ping')
        logger.info("✅ [MONGODB] Conexión exitosa a la Base de Datos")
    except Exception as e:
        logger.info(f"❌ [MONGODB] Fallo de conexión: {e}")