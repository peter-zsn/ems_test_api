from fastapi import FastAPI, WebSocketDisconnect, WebSocket
import uvicorn
import logging
from apps.routers import root_routers
from middlewares.auth_milldewares import AuthMiddleware
from loggers.logger import LOGGING_CONFIG

app = FastAPI(title='ems_rest_api')
app.add_middleware(
    AuthMiddleware
)

app.include_router(root_routers)
uvicorn.run(app=app, host='127.0.0.1', port=8080, log_config=LOGGING_CONFIG)

'''
uvicorn app:app --host 0.0.0.0 --port 8080 --workers 4 
'''