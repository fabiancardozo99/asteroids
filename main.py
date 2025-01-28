import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for p in updatable:
            p.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
        
            for bullet in shots:
                if asteroid.check_collision(bullet):
                    asteroid.split()
                    bullet.kill()

        # player.update(dt)
        screen.fill("black")
        for p in drawable:
            p.draw(screen)

        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()