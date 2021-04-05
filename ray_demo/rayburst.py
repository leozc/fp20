import ray
import time
import random
from ray.util import ActorPool
import asyncio


def say_hello() -> int:
    print ("Hello")
    return 1

@ray.remote
class CounterActor(object):
    def __init__(self):
        self.n = 0
        self._done = False

    async def increment(self):
        for i in range(1,20):
            await asyncio.sleep(random.randint(1, 3))
            self.n += 1
        self._done = True

    @ray.method(num_returns=1)
    async def read(self):
        return (self.n, self._done)



## An example for polling ray actors for their work progress.
if __name__ == "__main__":
    # patch
    # Hang here - and check out the ray worker errors as below
    # ~/.cache/pants/named_caches/pex_root/installed_wheels/a0d5c63d05cf2c837e5e8a0f410c1075f296d621/ray-1.0.1-cp38-cp38-macosx_10_13_x86_64.whl/ray/workers/default_worker.py", line 7, in <module>
    # import ray
    # ModuleNotFoundError: No module named 'ray'
    # Traceback (most recent call last):
    ray.init()
    counters = [
        CounterActor.options("c {}".format(x)).remote() for x in range(10)
    ]
    # pool = ActorPool(counters)
    # init x objects
    c_increased = [c.increment.remote() for c in counters] # call increase for these objects

    allDone= False
    while not allDone:
        array_of_count_done = ray.get([c.read.remote() for c in counters])
        allDone = all(map(lambda x: x[1], array_of_count_done))
        print(array_of_count_done)
        time.sleep(1)