from fastapi import WebSocket
import threading
from loggers.logger import setup_log
import time
import asyncio

logger = setup_log()

class TestWebSocketService(threading.Thread):
    def __init__(self) -> None:
        threading.Thread.__init__(self)
        self.clients = []
        self.stop_event = threading.Event()
        
    async def send_message(self, message):
        # tasks = []
        for client in self.clients:
            # task = asyncio.create_task(client.send_text(message))
            # tasks.append(task)
            await client.send_text(message)
        # await asyncio.gather(tasks)
    
    def run(self):
        if self.stopped():
            self.logger.info("Webhook stopped")
            return
        logger.info('TestWebSocketService start')
        i = 1
        try:
            tasks = []
            while True:
                i += 1
                logger.info('sleep ---- wait----')
                logger.info(i)
                logger.info(self.clients)
                if i % 5 == 0 and self.clients:
                    print(1111)
                    self.send_message(str(i))
                time.sleep(1) 
        except KeyboardInterrupt:
            self.stop()
                    
    def stop(self):
        logger.info("Waiting for the last data push finished")
        self.stop_event.set()
        
    def stopped(self):
        return self.stop_event.is_set()
        
        
    async def redis_push(self):
        pass
    
WebSocketService = TestWebSocketService()
