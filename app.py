from fastapi import FastAPI, WebSocketDisconnect, WebSocket
import uvicorn
import logging
from apps.routers import root_routers
from middlewares.auth_milldewares import AuthMiddleware
from loggers.logger import LOGGING_CONFIG
from libs.websocket_server import WebSocketService
app = FastAPI(title='ems_rest_api')
app.add_middleware(
    AuthMiddleware
)

@app.on_event("startup")
def start_up():
    print(123)

@app.on_event('shutdown')
def end():
    print(456)
    
# WebSocketService.setDaemon(True)
# WebSocketService.start()

app.include_router(root_routers)
uvicorn.run(app=app, host='127.0.0.1', port=8080, log_config=LOGGING_CONFIG)