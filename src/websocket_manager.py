from fastapi import WebSocket
from starlette.websockets import WebSocketState
from typing import List
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"🔌 Unity conectado. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            print("❌ Unity desconectado")

    async def broadcast(self, message: dict):
        """Envía mensaje JSON a todos los clientes (Unity)"""
        # Convertimos a JSON una sola vez
        json_msg = json.dumps(message, default=str)
        
        # Iteramos sobre una COPIA de la lista [:]
        # Esto es vital para poder eliminar elementos dentro del bucle sin romperlo
        for connection in self.active_connections[:]:
            try:
                # Intento de envío blindado
                if connection.client_state == WebSocketState.CONNECTED:
                    await connection.send_text(json_msg)
                else:
                    # Si el estado interno dice que no está conectado, limpiar
                    self.disconnect(connection)
            except Exception:
                # ESTRATEGIA DE SILENCIO:
                # Si falla por CUALQUIER razón (socket cerrado, error de red, timeout),
                # simplemente eliminamos la conexión y seguimos. No imprimimos error.
                self.disconnect(connection)

# Instancia global
manager = ConnectionManager()