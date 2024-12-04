import pygame
import sys
from player import Player
from mob import Mob

# Initialize Pygame
pygame.init()
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Maplestory Jump")
dt = 0  # Delta time

# Load assets
BACKGROUND = pygame.image.load("assets/GCGreenhouse.jpg")
pinkbean = pygame.image.load("assets/mob/standing.png").convert_alpha()
die_frames = [
    pygame.image.load(f"assets/mob/die.png").convert_alpha()
    for i in range(1, 5)
]

# Initialize player and mobs
player = Player(600, 510)
mobs = [
    Mob(710, 490, pinkbean, die_frames),
    Mob(1080, 570, pinkbean, die_frames),
    Mob(630, 140, pinkbean, die_frames),
]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    player.update(keys, dt)

    # Update mobs (check collision with the player)
    for mob in mobs:
        # Check for collision (player jumping on top of mob)
        if player.rect.colliderect(mob.rect) and player.rect.bottom <= mob.rect.top + 10 and player.jumping:
            mob.die()  # Trigger the dying state when the player lands on the mob

        mob.update()

    # Draw everything
    SCREEN.blit(BACKGROUND, (0, 0))
    player.draw(SCREEN)
    for mob in mobs:
        mob.draw(SCREEN)

    # Update the display and set frame rate
    pygame.display.update()
    dt = CLOCK.tick(60) / 1000  # Convert milliseconds to seconds
