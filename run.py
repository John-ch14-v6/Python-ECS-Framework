'''

Entity Component System framework (Python 3.10, PyGame 2.1.2)

Provided for free use without attribution under CC0

Core loop:
run()
... STATE_STACK()
... ... stack[-1].update()
... ... ... Input System
... ... ... ... Subsystems
... ... ... Update System
... ... ... ... Subsystems
... ... ... Render System
... ... ... ... Subsystems

... SOUND_MGR()
... ... update()

... clock.tick(FRAME_RATE)


'Jesus saith unto him, I am the way, the truth, and the life: no man cometh unto the Father, but by me.'
 - John 14:6 KJV

'''


import pygame as pg
import sys

from init import FRAME_RATE
from entities.entity_pool import POOL
from scripts.components import Close
from states.stack import STATE_STACK
from sound import SOUND_MGR


def run():
    clock = pg.time.Clock()
    STATE_STACK.start()
    SOUND_MGR.start()

    while not bool(POOL.grab(Close)):
        STATE_STACK.update()
        STATE_STACK.stack[-1].update()
        SOUND_MGR.update()
        clock.tick(FRAME_RATE)

    pg.quit()
    sys.exit()


if __name__ == '__main__':
    run()
