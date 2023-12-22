import pygame
from settings import *

# Define Tile class posessing an image and a position in the map
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        
        self.sprite_type = sprite_type # assign sprite type
        self.image = surface # assign image to tile
        self.rect = self.image.get_rect(topleft=pos) # assign space (a rectangle) to tile
        self.hitbox = self.rect.inflate(0, -10) # define hitbox (makes tile rectangle partly overlappable)