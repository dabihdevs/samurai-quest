import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer

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
        self.attack_sprites = pygame.sprite.Group() # particles
        self.attackable_sprites = pygame.sprite.Group() # enemies


        # Sprite setup
        self.create_map()

        # User interface
        self.ui = UI()

        # Particles
        self.animation_player = AnimationPlayer()

    
    # Create map
    def create_map(self):
        
        layouts = {
            'boundary' : import_csv_layout('../data/map_layers/map_floorblocks.csv'),
            'object' : import_csv_layout('../data/map_layers/map_objects.csv'),
            'entities' : import_csv_layout('../data/map_layers/map_entities.csv') 
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
                        if style == 'entities':
                            if col == "4":
                                self.player = Player(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic)
                            else:
                                if col == "0": monster_name = 'Beast'
                                elif col == "1": monster_name = 'Cyclope'
                                elif col == "2": monster_name = 'Ghost'
                                else: monster_name = 'Reptile'
                                Enemy(monster_name,
                                      (x,y),
                                      [self.visible_sprites, self.attackable_sprites],
                                      self.obstacle_sprites,
                                      self.damage_player,
                                      self.trigger_death_particles)
    
    # Create attack
    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])


    def create_magic(self, style, strength, cost):
        print(style)
        print(strength)
        print(cost)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

    def trigger_death_particles(self, pos):
        self.animation_player.create_particles('smoke', pos, self.visible_sprites)

    # Update and draw the game
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.ui.display(self.player)


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


    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)