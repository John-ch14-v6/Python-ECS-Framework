from entities.entity_pool import POOL
from systems.input import InputSystem
from systems.update import UpdateSystem
from sound import SoundSystem
from systems.render import RenderSystem

from systems.subs.keyboard import Keyboard


class State:
    def __init__(self):
        self.systems = {'input':    InputSystem(),
                        'update':   UpdateSystem(),
                        'sound':    SoundSystem(),
                        'render':   RenderSystem()}
        self.entity_pool = []

        self.add('input', Keyboard())

    def add(self, sub, system):
        self.systems[sub].add_sub(system)

    def remove(self, sub, system):
        self.systems[sub].remove_sub(system)

    def start(self):
        self.activate()
        for system in self.systems.values():
            system.start()

    def update(self):
        for system in self.systems.values():
            system.update()

    def activate(self):
        POOL.entities = self.entity_pool

    def deactivate(self):
        self.entity_pool = POOL.entities
