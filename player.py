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
            "jumping": pygame.image.load("assets/player/jump_0.png").convert_alpha(),
        }
        self.current_image = self.images["standing"]
        self.rect = self.current_image.get_rect(center=(x, y))
        self.velocity = 300
        self.frame_index = 0
        self.action = "standing"

        # Jumping attributes
        self.jumping = False
        self.jump_height = 20
        self.gravity = 1
        self.y_velocity = self.jump_height

    def update(self, keys, dt):
        # Movement logic
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
            if not self.jumping:
                self.action = "walking"
        else:
            if not self.jumping:
                self.action = "standing"

        # Jumping logic
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jumping = True

        if self.jumping:
            self.rect.centery -= self.y_velocity
            self.y_velocity -= self.gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.y_velocity = self.jump_height

        # Animation logic
        if self.action == "walking":
            self.frame_index += 10 * dt
            if self.frame_index >= len(self.images["walking"]):
                self.frame_index = 0
            self.current_image = self.images["walking"][int(self.frame_index)]
        elif self.jumping:
            self.current_image = self.images["jumping"]
        else:
            self.current_image = self.images["standing"]

    def draw(self, surface):
        surface.blit(self.current_image, self.rect)
