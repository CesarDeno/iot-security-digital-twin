from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Literal

class SecurityEvent(BaseModel):
    device_id: str
    # Estado actual de la puerta
    door_status: Literal["OPEN", "CLOSED"] 
    # Qué método se usó (Solo relevante si se acaba de abrir)
    access_method: Optional[Literal["KEYPAD", "NFC", "MANUAL"]] = None
    timestamp: Optional[datetime] = None