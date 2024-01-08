import pygame, sys
from settings import *
from level import Level

# Define game!
class Game:
    def __init__(self): 
    
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # set up space
        pygame.display.set_caption('Samurai Quest')
        self.clock = pygame.time.Clock() # set up time (clock)
        self.level = Level() # set up level
        
    # Define run action
    def run(self):
        while(True):
            # Close app if quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill('black') # display black screen
            self.level.run() # run level
            pygame.display.update()
            self.clock.tick(FPS) # start clock

# Run game
if __name__ == '__main__':
    game=Game()
    game.run()