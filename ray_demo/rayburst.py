import ray
import time
import random
from ray.util import ActorPool
import asyncio

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
    #
    #  Hang here, if ray is not globally installed (in your default venv?)
    ray.init()  
    
    # init x objects
    counters = [
        CounterActor.options("c {}".format(x)).remote() for x in range(10)
    ]

    # pool = ActorPool(counters)
    c_increased = [c.increment.remote() for c in counters] # call increase for these objects

    allDone= False
    while not allDone:
        array_of_count_done = ray.get([c.read.remote() for c in counters])
        allDone = all(map(lambda x: x[1], array_of_count_done))
        print(array_of_count_done)
        time.sleep(1)

    ray.shutdown()
