
from helloworld.config import load_config
from helloworld.greet.greeting import Greeter

import ray
import time
import random

def say_hello() -> int:
    print ("Hello")
    return 1

@ray.remote
class Counter(object):
    def __init__(self):
        self.n = 0

    def increment(self):
        self.n += 1
        time.sleep( random.randint(1, 5) )

    def read(self):
        return self.n

# on Mac brew services restart redis
# spin local redis `docker run -v redis.conf:/usr/local/etc/redis/redis.conf -d --name redis -p 6379:6379  redis:5.0.10  redis-server /usr/local/etc/redis/redis.conf`
if __name__ == "__main__":
    say_hello()
    # see redis.conf
    ray.init(address="localhost:6379", _redis_password="testtesttest")

    for i in range(1,20):
        counters = [Counter.remote() for i in range(4)]
        [c.increment.remote() for c in counters]
        futures = [c.read.remote() for c in counters]
        print(ray.get(futures))
    ray.shutdown()