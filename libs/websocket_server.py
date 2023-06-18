from fastapi import WebSocket
import threading
from loggers.logger import setup_log
import time
import asyncio

logger = setup_log()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
 
    async def connect(self, websocket: WebSocket):
        self.active_connections.append(websocket)
 
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
 
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
 
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            pass
        
WebSocketService = ConnectionManager()
