import pygame as pg
from entities.entity import Entity
from entities.entity_pool import POOL
from scripts.components import Close
from systems.system import SubSystem


class Keyboard(SubSystem):
    def __init__(self):
        super().__init__()

    def update(self, events):
        for event in events:
            if event.type == pg.QUIT:
                POOL.add(close_app())

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                POOL.add(close_app())


def close_app():
    closer = Entity()
    closer.add(Close())
    return closer
