from fastapi import APIRouter, WebSocket
from websockets.exceptions import ConnectionClosedError
from starlette.requests import Request
from loggers.logger import setup_log
import asyncio
import aioredis


logger = setup_log()
websocket_router = APIRouter()

redis_client = aioredis.from_url("redis://localhost")

@websocket_router.post('/ping', summary='websocket接口注释', description='接口描述', tags=['systems'])
async def ping(username: str = '', password: str = ''):
    """
    登录
    :param username: 用户名
    :param password: 密码
    :return: 是否成功
    """
    logger.info(f'username:{username}')
    logger.error(f'password{password}')
    # data = await request.json()
    # print(data)
    return {'status': 'ok'}


@websocket_router.websocket('/test')
async def test(websocket: WebSocket):
    await websocket.accept()
    try:
        data = await websocket.receive_text()
        logger.info(data)
        i = 1
        logger.info(data)
        while True:
            i += 1
            message = f'test-{i}'
            await websocket.send_text(message) 
            await asyncio.sleep(1)
    except Exception as e:
        # logger.info(e.__str__())
        # if e.__str__() == 'no close frame received or sent':
        #     logger.info(111111111111)
        if isinstance(e, ConnectionClosedError):
            logger.error('websocker disconnect')
        logger.info(e)
    # return {}
    


@websocket_router.websocket('/test2')
async def test2(websocket: WebSocket):
    await websocket.accept()
    try:
        data = await websocket.receive_text()
        logger.info(data)
        pubsub = redis_client.pubsub()
        await pubsub.subscribe('aaa',)
        while True:
            message = await pubsub.get_message()
            if message:
                if type(message['data']) == bytes:
                    await websocket.send_text(message['data'].decode())
                else:
                    await websocket.send_text('初始数据')
    except Exception as e:
        if isinstance(e, ConnectionClosedError):
            logger.error('websocker disconnect')
        await pubsub.close()
        logger.error(e)
    return