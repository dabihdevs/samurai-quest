import pygame
from support import import_folder

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # Attack
            'cut': import_folder("../graphics/particles/cut"),
            'claw': import_folder("../graphics/particles/claw"),
            'slash': import_folder("../graphics/particles/slash"),

            # Magic
            'thunder': import_folder("../graphics/particles/thunder/frames", scale=(20,28)),
            'heal': import_folder("../graphics/particles/heal/frames"),

            # Monster deaths
            'smoke': import_folder("../graphics/particles/smoke")
        }

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.image.get_rect[self.frame_index]

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()