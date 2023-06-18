from fastapi import APIRouter, WebSocket
from websockets.exceptions import ConnectionClosedError
from starlette.requests import Request
from loggers.logger import setup_log
import asyncio


logger = setup_log()
websocket_router = APIRouter()


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