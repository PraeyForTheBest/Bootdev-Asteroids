import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)



    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    while True == True: # infinite loop to run the game
        for event in pygame.event.get(): #for loop to have the game check to see if the program was quit
            if event.type == pygame.QUIT:
                return
        screen.fill(0) #draws a black screen
        for object in drawable:
            object.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game Over")
                pygame.quit()
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()

        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # Checks how much time in seconds has passed since the last time it was called

if __name__ == "__main__":
    main()
