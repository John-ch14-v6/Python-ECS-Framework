import time
from init import FRAME_RATE
from systems.system import System


class UpdateSystem(System):
    def __init__(self):
        super().__init__()
        self.prev_time = time.time()

    def update(self):
        now = time.time()
        dt = (now - self.prev_time) * FRAME_RATE
        self.prev_time = now

        print(f'FPS: {int(FRAME_RATE / dt)}')

        for system in self.subsystems:
            system.update(dt)
