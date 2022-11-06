from entities.entity_pool import POOL
from systems.input import InputSystem
from systems.update import UpdateSystem
from systems.render import RenderSystem

from systems.subs.keyboard import Keyboard
from systems.subs.mouse import Mouse


class State:
    def __init__(self):
        self.systems = {'input':    InputSystem(),
                        'update':   UpdateSystem(),
                        'render':   RenderSystem()}
        self.entity_pool = []

        self.add('input', Keyboard())
        self.add('input', Mouse())

    def add(self, system, sub):
        self.systems[system].add_sub(sub)

    def remove(self, system, sub):
        self.systems[system].remove_sub(sub)

    def start(self):
        for system in self.systems.values():
            system.start()

    def update(self):
        for system in self.systems.values():
            system.update()

    def activate(self):
        POOL.entities = self.entity_pool

    def deactivate(self):
        self.entity_pool = POOL.entities
