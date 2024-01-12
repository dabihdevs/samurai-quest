import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self, speed):
    
        # Normalize vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        # Update entity position based on input
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
    