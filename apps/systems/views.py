from fastapi import APIRouter
from starlette.requests import Request
from loggers.logger import setup_log
import time
import asyncio
from apps.websockets.views import call
import threading,_thread

logger = setup_log()
systems = APIRouter()

@systems.post('/ping', summary='接口注释', description='接口描述', tags=['systems'])
async def ping(username: str = '', password: str = ''):
    """
    登录
    :param username: 用户名
    :param password: 密码
    :return: 是否成功
    """
    logger.info(f'username:{username}')
    logger.info(f'username:{username}')
    logger.error(f'password{password}')
    _thread.start_new_thread(call, () )

    # data = await request.json()
    # print(data)
    return {'status': 'ok'}


    
    
    
    