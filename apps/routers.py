from fastapi import APIRouter
from apps.index import index_router
from apps.systems.routers import system_routers

root_routers = APIRouter()
root_routers.include_router(index_router)
root_routers.include_router(system_routers)


