import pygame

class Mob:
    alive_mobs = []
    dead_mobs = []

    def __init__(self, x, y, alive_image, dead_image):
        self.x = x
        self.y = y
        self.alive_image = alive_image
        self.dead_image = dead_image
        self.is_alive = True
        Mob.alive_mobs.append(self)
        

    def remove(self):
        if self.is_alive:
            self.is_alive = False
            Mob.alive_mobs.remove(self)
            Mob.dead_mobs.append(self)

    def update(self):
        # Add movement or AI logic for mobs here if needed
        pass

