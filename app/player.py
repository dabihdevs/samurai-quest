import pygame
from settings import *
from support import import_folder
from entity import Entity

# Define Player class posessing an image and a position in the map
class Player(Entity):

    # Import player assets
    def import_player_assets(self):
        character_path = "../graphics/player/"
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path, scale=(64, 64))

    
    # Initialize Player
    def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack, create_magic):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player/down_idle/down_idle.png').convert_alpha() # assign image to player
        self.rect = self.image.get_rect(topleft=pos) # assign space (a rectangle) to player
        self.hitbox = self.rect.inflate(0, -10) # define hitbox (makes player rectangle partly overlappable)

        # Graphics setup
        self.import_player_assets()
        self.status = 'down'

        # Movement
        self.attacking = False
        self.attack_cooldown = 400 # ms it takes before attacking again
        self.attack_time = None
        
        self.obstacle_sprites = obstacle_sprites

        # Weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # Magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # Stats
        self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'magic': 4, 'speed': 5}
        self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'magic': 10, 'speed': 10}
        self.upgrade_cost = {'health': 100, 'energy': 100, 'attack': 100, 'magic': 100, 'speed': 100} # XPs
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 500 # XPs
        self.speed = self.stats['speed']

        # Damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invincibility_duration = 500

        # Import a sound
        self.weapon_attack_sound = pygame.mixer.Sound('../sounds/Game/Sword.wav')
        self.weapon_attack_sound.set_volume(0.4)
    

    # Input from the keyboard
    def input(self):
        if not self.attacking:        
            # Store pressed key
            keys = pygame.key.get_pressed()
            
            # Assign direction vector to the 4 directional keys:
            # Along y axis
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
            
            # Along x axis            
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # Attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                self.weapon_attack_sound.play()
                
            # Magic input
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                style = list(magic_data.keys())[self.magic_index]
                strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
                cost = list(magic_data.values())[self.magic_index]['cost']
                self.create_magic(style, strength, cost)

            # Select weapon
            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()

                if self.weapon_index < len(list(weapon_data.keys())) - 1:

                        self.weapon_index += 1
                else:
                    self.weapon_index = 0

                self.weapon = list(weapon_data.keys())[self.weapon_index]

            # Select spell
            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()

                if self.magic_index < len(list(magic_data.keys())) - 1:

                        self.magic_index += 1
                else:
                    self.magic_index = 0

                self.magic = list(magic_data.keys())[self.magic_index]


    # Get status
    def get_status(self):

        # Idle
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        # Attacking
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    # Cooldown times
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
                self.attacking = False
                self.destroy_attack()

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.vulnerable = True

    # Animate the player image
    def animate(self):
        animation = self.animations[self.status]

        # Loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

        # Flicker when hit
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)


    def get_full_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage

    def get_full_magic_damage(self):
        base_damage = self.stats['magic']
        spell_damage = magic_data[self.magic]['strength']
        return base_damage + spell_damage

    def get_value_by_index(self, index):
        return list(self.stats.values())[index]

    def get_cost_by_index(self, index):
        return list(self.upgrade_cost.values())[index]
            

    def energy_recovery(self):
        if self.energy < self.stats['energy']:
            self.energy += 0.01 * self.stats['magic']
        else:
            self.energy = self.stats['energy']

    # Update player
    def update(self):
        self.input() # get and store keyboard input
        self.cooldowns() # set timer and cooldowns
        self.get_status() # get player status
        self.animate() # set player animation
        self.move(self.stats['speed']) # move player based on stored input
        self.energy_recovery()
        