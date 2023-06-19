import asyncio
import websockets
import time

async def permanant_conn():
    wss_url = 'ws://localhost:8080/ws/test_publish'
    async with websockets.connect(wss_url) as websocket:
        message = "shuainan"
        await websocket.send(message)
        while True:
            result = await websocket.recv()
            print(result)
        
asyncio.get_event_loop().run_until_complete(permanant_conn())