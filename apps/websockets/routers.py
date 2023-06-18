from fastapi import APIRouter
from apps.websockets.views import websocket_router

ws_routers = APIRouter()
ws_routers.include_router(websocket_router)


