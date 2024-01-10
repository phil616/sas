from asyncio import sleep

from core.background import generate_background_scheduler
from core.logcontroller import Logger

async def waiting():
    await sleep(5)
class SharedMemory:
    """
    这个类是一个运行时共享的库
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SharedMemory, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.global_switch = True
        self.global_counter = 1
        self.crt_state = "a"


    async def crt(self,r):
        await waiting()
        self.crt_state = r
        await waiting()
        return self.crt_state


class GlobalState:
    def __init__(self):
        self.runtime = SharedMemory()
        ...

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__.get(item)


G_state = GlobalState()


def get_global_state() -> GlobalState:
    return G_state



runtime_info = {}
syslog = Logger("system").getLogger
scheduler = generate_background_scheduler()
