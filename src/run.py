import sys
import asyncio

# Forza la política de eventos SelectorEventLoop antes de cargar cualquier otra librería.
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import uvicorn

if __name__ == "__main__":
    print("🚀 Iniciando Servidor IoT...")
    
    # Ejecutar Uvicorn programáticamente
    # 'main:app' apunta a la instancia FastAPI en main.py
    uvicorn.run(
        "main:app", 
        host="localhost", 
        port=8000, 
        reload=True,
        log_level="info"
    )