import pygame as pg
from systems.system import System


class InputSystem(System):
    def __init__(self):
        super().__init__()

    def update(self):
        events = pg.event.get()
        for system in self.subsystems:
            system.update(events)
