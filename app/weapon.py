import pygame

# Define weapon class
class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]

        # Graphic
        full_path = f'../graphics/weapons/{player.weapon}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        if player.weapon == 'Katana':
            if direction == 'down' or direction == 'up':
                self.image = pygame.transform.scale(self.image, (20, 32))
            else:
                self.image = pygame.transform.scale(self.image, (32, 20))
        else:
            if direction == 'down' or direction == 'up':
                self.image = pygame.transform.scale(self.image, (30, 64))
            else:
                self.image = pygame.transform.scale(self.image, (64, 30))

        # Placement
        if player.weapon == 'Katana':
            if direction == 'right':
                self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-3, 16))
            elif direction == 'left':
                self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(3, 16))
            elif direction == 'down':
                self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10, 0))
            else:
                self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-17, 3))
        else:
            if direction == 'right':
                self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-5, 13))
            elif direction == 'left':
                self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(5, 13))
            elif direction == 'down':
                self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10, 0))
            else:
                self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-19, 5))