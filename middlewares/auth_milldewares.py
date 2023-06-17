import typing
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp
from fastapi import Request, Response, HTTPException
import json


    
class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        name = request.query_params.get('name', '')
        token = request.headers.get('token', '')
        print(request.method)
        print(token, 'token')
        print(name, '路由参数')
        print(request.url, 'url')
        print(request.url.path, '路由')
        if name == 'quit':
            response = Response(status_code=401, content=json.dumps({'test': '123'}), media_type='application/json')
            return response
        response = await call_next(request)
        response.headers['test'] = 'test'
        return response        
    