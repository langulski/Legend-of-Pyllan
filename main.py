import pygame as pg
from settings import *
import sys
from debug import debug
from level import Level


class Game():
    def __init__(self):
        pg.init()
        self.screen =  pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption('Adventure game')
        self.clock = pg.time.Clock()
        self.level = Level()
    def run(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level.run()
            # debug('test debug tool')
            pg.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
