import pygame
from mob import Mob
from player import Player

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mob vs Player")
clock = pygame.time.Clock()
running = True
dt = 0  # Delta time

# Load assets
bg = pygame.image.load("assets/GCGreenhouse.jpg")
pinkbean = pygame.image.load("assets/mob/standing.png")
die = pygame.image.load("assets/mob/die.png")

# Initialize player and mobs starting position
player = Player(100, 510)  
mobs = [
    Mob(710, 490, pinkbean, die),
    Mob(1080, 570, pinkbean, die),
    Mob(630, 140, pinkbean, die),
]

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player input
    keys = pygame.key.get_pressed()

    # Update player and mobs
    player.update(keys, dt)
    for critter in mobs:
        critter.update()

    # Check for collisions
    for critter in Mob.alive_mobs:
        in_x = (critter.x - 50) <= player.rect.centerx <= (critter.x + 50)
        in_y = (critter.y - 50) <= player.rect.centery <= (critter.y + 50)
        if in_x and in_y:
            critter.remove()

    # Check if all mobs are dead
    if len(Mob.alive_mobs) == 0:
        running = False

    # Drawing
    screen.fill("light pink")
    screen.blit(bg, (0, 0))
    player.draw(screen)
    for critter in Mob.alive_mobs:
        screen.blit(critter.alive_image, (critter.x, critter.y))
    for critter in Mob.dead_mobs:
        screen.blit(critter.dead_image, (critter.x, critter.y))

    # Update display
    pygame.display.flip()

    # Limit FPS and calculate delta time
    dt = clock.tick(60) / 1000

pygame.quit()
