from fastapi import APIRouter
from apps.systems.views import systems

system_routers = APIRouter()
system_routers.include_router(systems)


