import pygame as pg 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice

class Level:
    def __init__(self):
        # get the display:
        self.display_surface = pg.display.get_surface()

        #sprite group:
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pg.sprite.Group()
    
        #sprite setup
        self.create_map()
    
    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('./map/map_Grass.csv'),
            'object': import_csv_layout('./map/map_Objects.csv')
        }
        graphics  = {
            'grass' : import_folder('./graphics/Grass'),
            'objects': import_folder('./graphics/Objects')
        }

        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x =  col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacles_sprites],'invisible')
                        if style =='grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites],'grass',random_grass_image)
                        if style =='object':
                            surf  = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites],'object',surf)
                            
        #         if col == 'x':
        #             Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
        #         if col =='p':
        #             self.player = Player((x,y),[self.visible_sprites],self.obstacles_sprites)
        self.player = Player((2000,1500),[self.visible_sprites],self.obstacles_sprites)
                



    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # debug(self.player.direction)

class YSortCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2(100,200)
    
    #creating the floor
        self.floor_surface =  pg.image.load('./graphics/tilemap/ground.png').convert()
        self.floor_rect =  self.floor_surface.get_rect(topleft=(0,0))
    
    def custom_draw(self,player):
        #offset
        self.offset.x =  player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)
        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
    
