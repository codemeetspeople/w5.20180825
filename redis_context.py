import redis
import threading
import random
from time import sleep

class RedisPool:
    def __init__(self, host='127.0.0.1', port=6379, db=0):
        self.pool = redis.ConnectionPool(
            host=host, port=port, db=db, decode_responses=True
        )
        self.connection = None

    def __enter__(self):
        self.connection = redis.StrictRedis(
            connection_pool=self.pool
        )
        print(id(self.connection))
        return self.connection

    def __exit__(self, *args, **kwargs):
        print('exit')
        try:
            print(f'delete: {id(self.connection)}')
            del self.connection
        except AttributeError:
            pass


redis_pool = RedisPool()

def write_in_redis(pool, key, value):
    with pool as connection:
        connection.set(key, value)

# with redis_pool as connection:
#     keys = connection.keys('key_*')
#     for key in keys:
#         connection.delete(key)

threads = []
for i in range(10):
    threads.append(threading.Thread(
        target=write_in_redis, args=[
            redis_pool, f'key_{i}', f'value_{random.randint(1, 1000)}'
        ]
    ))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# with redis_pool as connection:
#     keys = connection.keys('key_*')
#     for key in sorted(keys):
#         print(f'{key}: {connection.get(key)}')
