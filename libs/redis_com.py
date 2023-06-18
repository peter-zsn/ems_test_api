import redis
from rejson import Client, Path
import time

class RedisClient:
    def __init__(self):
        # startup_nodes = [{ "host": config['CONFIG_REDIS']['host'], "port": str(config['CONFIG_REDIS']['port']) }]
        pool = redis.ConnectionPool(
            host='127.0.0.1',
            port='6379',
            db='0')
        self.redis_client = redis.Redis(connection_pool=pool)
        self.rejson_client = Client(host='127.0.0.1', port='6379',
                                    decode_responses=True)

    def set(self, key, value, ex=None):
        self.redis_client.set(key, value)
        if ex:
            self.redis_client.expire(key, ex)

    def set_1min(self, key, value):
        if isinstance(value, dict):
            value['redistime'] = time.time()
        self.set(key, value, ex=60 * 10)

    def get(self, key, path='.'):
        try:
            if path.strip() == '.':
                return self.redis_client.get(key)
            else:
                return self.redis_client.get(key)
        except:
            return None

    def exists(self, key):
        result = self.redis_client.get(key)
        if result:
            return True
        else:
            return False

    def lrange(self, name, start=0, end=-1):
        byte_res = self.redis_client.lrange(name, start, end)
        result = [json.loads(i) for i in byte_res]
        return result

    def lgetmax(self, name, hkey=None):
        key = self.redis_client.llen(name)
        # print(key)
        if (key > 0):
            for i in range(key - 1, -1, -1):
                item = json.loads(self.redis_client.lindex(name, i))
                if (hkey is None):
                    return item
                if (item[0] <= hkey):
                    return item
            return None
        else:
            return None

    def get_keys(self, re_str):
        '''
            传入一个正则表达式，返回匹配的key
        '''
        keys = self.redis_client.scan_iter(match=f"{re_str}")
        return [str(key) for key in keys]


if __name__ == "__main__":
    redis_client = RedisClient()
    redis_client.set('test', 123)
    a = redis_client.get('test')
    print(a)
