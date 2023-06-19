from fastapi import FastAPI, WebSocketDisconnect, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from threading import Thread
import aioredis
import uvicorn
from apps.routers import root_routers
from middlewares.auth_milldewares import AuthMiddleware
from loggers.logger import LOGGING_CONFIG

app = FastAPI(title='ems_rest_api1111')

# 处理跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    AuthMiddleware
)


# print(11111)
# @app.on_event("startup")
# def start_up():
#     print(123)

# @app.on_event('shutdown')
# def end():
#     print(456)
    
app.include_router(root_routers)
uvicorn.run(app=app, host='127.0.0.1', port=8080, log_config=LOGGING_CONFIG)

