# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    Clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = (Clock.tick(60)) / 1000 # Frame Limiter
#stops the program running unless started directly
if __name__ == "__main__":
    main()