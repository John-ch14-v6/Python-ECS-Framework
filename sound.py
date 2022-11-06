import pygame as pg

from scripts.components import *
from systems.system import System


SFX_LIB = {

}


class SoundSystem(System):
    def __init__(self):
        super().__init__()
        # pg.mixer.music.load('theme.mp3')

    def start(self):
        pg.mixer.music.play(loops=-1, fade_ms=1200)
        pass

    def update(self):
        pass


SOUND_MGR = SoundSystem()
