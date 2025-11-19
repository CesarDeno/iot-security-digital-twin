from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL, DB_NAME, COLLECTION_NAME

# Inicialización del cliente
client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

async def save_sensor_data(data: dict):
    """Guarda los datos del sensor en MongoDB"""
    try:
        await collection.insert_one(data)
    except Exception as e:
        print(f"Error guardando en DB: {e}")