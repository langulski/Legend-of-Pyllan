import pygame as pg 
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        # get the display:
        self.display_surface = pg.display.get_surface()

        #sprite group:
        self.visible_sprites = pg.sprite.Group()
        self.obstacles_sprites = pg.sprite.Group()
    
        #sprite setup
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x =  col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
                if col =='p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacles_sprites)
                



    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)