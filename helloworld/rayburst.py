
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


if __name__ == "__main__":
    #patch 
    import resource
    # Related to https://github.com/ray-project/ray/issues/12033
    # NOTE: sure your outter env install the same version of ray
    print ("========= bootstrap")
    print (resource.getrlimit(resource.RLIMIT_NOFILE)) # this number doesnt look right 
    resource.setrlimit(resource.RLIMIT_NOFILE,(1024,655360))
    print ("========= endBootstrap")
    say_hello()
    # Hang here
    ray.init()
    counters = [Counter.remote() for i in range(4)]

    for i in range(1,20):
         [c.increment.remote() for c in counters]
         futures = [c.read.remote() for c in counters]
         print(ray.get(futures))
    ray.shutdown()