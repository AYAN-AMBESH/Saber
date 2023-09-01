
from saber.base import scanner


import threading

LOCK= threading.Lock()

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with LOCK:
                if cls not in cls._instances:
                    cls._instances[cls] = super(
                        Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]




class saber(metaclass=Singleton):
    def __init__(self) -> None:
        pass
    
    def run(self):
        pass

