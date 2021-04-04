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
        time.sleep( random.randint(1, 3) )

    def read(self):
        return self.n


if __name__ == "__main__":
    #patch
    # Hang here - and check out the ray worker errors as below
    # ~/.cache/pants/named_caches/pex_root/installed_wheels/a0d5c63d05cf2c837e5e8a0f410c1075f296d621/ray-1.0.1-cp38-cp38-macosx_10_13_x86_64.whl/ray/workers/default_worker.py", line 7, in <module>
    # import ray
    # ModuleNotFoundError: No module named 'ray'
    # Traceback (most recent call last):
    ray.init()
