import pygame as pg


pg.init()

SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
SCREEN_RECT = SCREEN.get_rect()
TRANSPARENT = (0, 0, 0)
SCREEN.set_colorkey(TRANSPARENT)

FRAME_RATE = 60
