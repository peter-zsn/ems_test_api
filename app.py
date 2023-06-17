from fastapi import FastAPI
import uvicorn
from apps.routers import root_routers
from middlewares.auth_milldewares import AuthMiddleware

app = FastAPI(title='ems_rest_api')
app.add_middleware(
    AuthMiddleware
)

app.include_router(root_routers)
uvicorn.run(app=app, host='127.0.0.1', port=8080)
