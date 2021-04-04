import ray
import time
import random

def say_hello() -> int:
    print ("Hello")
    return 1

@ray.remote
class CounterActor(object):
    def __init__(self):
        self.n = 0

    def increment(self):
        for i in range(1,20):
            time.sleep( random.randint(2, 7) )
            self.n += random.randint(1, 10)

    @ray.method(num_returns=1)
    def read(self):
        return self.n


if __name__ == "__main__":
    # patch
    # Hang here - and check out the ray worker errors as below
    # ~/.cache/pants/named_caches/pex_root/installed_wheels/a0d5c63d05cf2c837e5e8a0f410c1075f296d621/ray-1.0.1-cp38-cp38-macosx_10_13_x86_64.whl/ray/workers/default_worker.py", line 7, in <module>
    # import ray
    # ModuleNotFoundError: No module named 'ray'
    # Traceback (most recent call last):
    ray.init()
    counters = [
        CounterActor.options("c {}".format(x)).remote() for x in range(100)
    ]  
    # init x objects
    c_increased = [c.increment.remote() for c in counters] # call increase for these objects

    for i in range(1,10): # keep reading
        c_read = [c.read.remote() for c in counters]
        print(ray.get(c_read))
        time.sleep(1)