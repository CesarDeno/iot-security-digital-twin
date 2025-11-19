import uvicorn
import asyncio
import sys

if __name__ == "__main__":
    # --- FIX CRÍTICO PARA WINDOWS ---
    # Forza el uso de la política de bucle 'Selector' en lugar de 'Proactor'.
    # Esto evita errores de "Socket Closed" y "WinError 10053" con MQTT/WebSockets.
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Ejecutar Uvicorn programáticamente
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )