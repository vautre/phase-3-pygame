import pygame

class Mob:
    alive_mobs = []
    dead_mobs = []

    def __init__(self, x, y, alive_image, dead_image):
        self.x = x
        self.y = y
        self.alive_image = alive_image
        self.dead_image = dead_image  # List of frames for dying animation
        self.width = alive_image.get_width()
        self.height = alive_image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # For collision
        self.is_alive = True
        self.dead_animation_index = 0
        self.dead_animation_speed = 0.1  # Controls the speed of the dying animation
        self.dead_timer = 0  # Timer to track the death duration
        Mob.alive_mobs.append(self)

    def die(self):
        if self.is_alive:
            self.is_alive = False
            self.dead_animation_index = 0  # Reset dying animation
            self.dead_timer = 0  # Reset the death timer
            Mob.alive_mobs.remove(self)  # Remove from alive mobs list
            Mob.dead_mobs.append(self)  # Optionally keep in dead_mobs

    def update(self):
        if not self.is_alive:
            self.dead_timer += 1  # Increment the death timer
            self.dead_animation_index += self.dead_animation_speed
            if self.dead_animation_index >= len(self.dead_image):  # If all frames have been shown
                self.dead_animation_index = len(self.dead_image) - 1  # Stop at the last frame
                if self.dead_timer > 60:  # Wait for 1 second before respawning (adjust as needed)
                    self.respawn()  # Respawn the mob

        # Movement logic (leftward movement)
        self.x -= 2
        if self.x < -self.width:  # Respawn mob if off-screen
            self.x = 1280
        self.rect.topleft = (self.x, self.y)  # Update rect position

    def respawn(self):
        self.is_alive = True
        self.dead_timer = 0
        self.x = 1280  # Reset to initial spawn position
        self.y = 490   # Or any desired position
        Mob.alive_mobs.append(self)  # Add back to the alive mobs list
        Mob.dead_mobs.remove(self)   # Remove from the dead mobs list

    def draw(self, screen):
        if self.is_alive:
            screen.blit(self.alive_image, (self.x, self.y))
        else:
            # Draw the current frame of the dying animation
            screen.blit(self.dead_image[int(self.dead_animation_index)], (self.x, self.y))
