import pygame
from settings import *

# Define Player class posessing an image and a position in the map
class Player(pygame.sprite.Sprite):
    
    # Initialize Player
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/player.png').convert_alpha() # assign image to player
        self.rect = self.image.get_rect(topleft=pos) # assign space (a rectangle) to player
        self.hitbox = self.rect.inflate(0, -26) # define hitbox (makes player rectangle partly overlappable)

        self.direction = pygame.math.Vector2() # initialize 2x1 vector indicating direction
        self.speed = 5 # initialize movement speed
        
        self.obstacle_sprites = obstacle_sprites
        
    # Input from the keyboard
    def input(self):
        
        # Store pressed key
        keys = pygame.key.get_pressed()
        
        # Assign direction vector to the 4 directional keys:
        # Along y axis
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        # Along x axis            
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    # Movement action
    def move(self, speed):
    
        # Normalize vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        # Update player position based on input
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        
    
    # Collision method
    def collision(self, direction):
    
        # Do not overlap player and sprites when they collide
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving upwards
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0: # moving downwards
                        self.hitbox.top = sprite.hitbox.bottom
    
    # Update player
    def update(self):
        self.input() # get and store keyboard input
        self.move(self.speed) # move player based on stored input
        