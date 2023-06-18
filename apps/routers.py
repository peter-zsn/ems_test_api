from fastapi import APIRouter
from apps.index import index_router
from apps.systems.routers import system_routers
from apps.websockets.routers import ws_routers

root_routers = APIRouter()
root_routers.include_router(index_router)
root_routers.include_router(system_routers, prefix='/systems')
root_routers.include_router(ws_routers, prefix='/ws')

