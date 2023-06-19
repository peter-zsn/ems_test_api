from collections.abc import Callable, Iterable, Mapping
from typing import Any
from fastapi import WebSocket
import threading
from loggers.logger import setup_log
import time
import asyncio
import aioredis
# redis_client = aioredis.from_url("redis://localhost")


# global WebSocketServiceList
WebSocketServiceList = set()    
WebSocketServiceListCalling = False

# async def test_publish(webSocketServiceList):
#     try:
#         # while True:
#         print(len(webSocketServiceList), 12312312)
#         await asyncio.sleep(1)
#         # pubsub = redis_client.pubsub()
#         # await pubsub.subscribe('aaa')
#         # while True:
#         #     message = await pubsub.get_message()
#         #     if message:
#         #         print(len(webSocketServiceList))
#         #         for client in webSocketServiceList:
#         #             print(client)
#         #             if type(message['data']) == bytes:
#         #                 await client.send_text(message['data'].decode())
#         #             else:
#         #                 await client.send_text('初始数据')
#     except Exception as e:
#         print(e)
#         pass
  


# def call():
#     print("call")
#     global WebSocketServiceList
#     loop=asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     tasks=[test_publish(WebSocketServiceList)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()
#     while True:
#         print(len(WebSocketServiceList), 'call')
#         time.sleep(1)
       