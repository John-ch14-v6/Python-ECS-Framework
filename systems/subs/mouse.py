import pygame as pg

from scripts.components import *
from systems.system import SubSystem


class Mouse(SubSystem):
    def __init__(self):
        super().__init__()

    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                pass

            if event.type == pg.MOUSEBUTTONUP:
                pass
