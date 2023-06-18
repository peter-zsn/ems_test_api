import aioredis

async def test():
    conn = await aioredis.create_connection(('localhost', 6379))
    channel = aioredis.Channel('aaa', is_pattern=False)
    await conn.execute_pubsub('subscribe', channel)
    return channel, conn

