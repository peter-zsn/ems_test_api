from fastapi import APIRouter
from starlette.requests import Request


systems = APIRouter()

@systems.post('/ping', summary='接口注释', description='接口描述', tags=['systems'])
async def ping(username: str = '', password: str = ''):
    """
    登录
    :param username: 用户名
    :param password: 密码
    :return: 是否成功
    """
    print(username, password)
    # data = await request.json()
    # print(data)
    return {'status': 'ok'}