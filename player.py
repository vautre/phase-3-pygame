import pygame

class Player:
    def __init__(self, x, y):
        self.images = {
            "standing": pygame.image.load("assets/player/standing.png").convert_alpha(),
            "walking": [
                pygame.image.load("assets/player/walk_1.png").convert_alpha(),
                pygame.image.load("assets/player/walk_2.png").convert_alpha(),
                pygame.image.load("assets/player/walk_3.png").convert_alpha(),
                pygame.image.load("assets/player/walk_4.png").convert_alpha(),
            ],
        }
        self.current_image = self.images["standing"]
        self.rect = self.current_image.get_rect(center=(x, y))
        self.velocity = 300
        self.frame_index = 0
        self.action = "standing"

    def update(self, keys, dt):
        # Movement and animation logic
        movement = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            movement.y = -1
        if keys[pygame.K_s]:
            movement.y = 1
        if keys[pygame.K_a]:
            movement.x = -1
        if keys[pygame.K_d]:
            movement.x = 1

        if movement.length() > 0:
            movement = movement.normalize()
            self.rect.centerx += movement.x * self.velocity * dt
            self.rect.centery += movement.y * self.velocity * dt
            self.action = "walking"
        else:
            self.action = "standing"

        # Animation logic
        if self.action == "walking":
            self.frame_index += 10 * dt
            if self.frame_index >= len(self.images["walking"]):
                self.frame_index = 0
            self.current_image = self.images["walking"][int(self.frame_index)]
        else:
            self.current_image = self.images["standing"]

    def draw(self, surface):
        surface.blit(self.current_image, self.rect)
