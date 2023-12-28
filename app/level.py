import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from weapon import Weapon

class Level:

    # Initialize class
    def __init__(self):
        
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # Attack sprites
        self.current_attack = None

        # Sprite setup
        self.create_map()
    
    # Create map
    def create_map(self):
        
        layouts = {
            'boundary': import_csv_layout('../data/map_layers/map_floorblocks.csv'),
            'object' : import_csv_layout('../data/map_layers/map_objects.csv')
        }

        graphics = {
            'object' : import_folder('../graphics/objects')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')
                        if style == 'object':
                            surf = graphics['object'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'object', surface=surf)
                    
        self.player = Player((384,2432), [self.visible_sprites], self.obstacle_sprites, self.create_attack, self.destroy_attack)
    
    # Create attack
    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None


    # Update and draw the game
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

# Create camera following the player       
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        # General setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)
        
        # Creating the floor
        self.floor_surf = pygame.image.load("../graphics/map/ground.png").convert()
        self.floor_surf = pygame.transform.scale(self.floor_surf, (2560, 2560))
        self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))
        
    def custom_draw(self, player):
    
        # Get offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        # Drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
    
        # Add offset
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)