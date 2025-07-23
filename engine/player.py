import pygame

class Player:
    def __init__(self, position, game_map):
        self.x, self.y = position
        self.image = pygame.image.load("assets/characters/player.png")
        self.speed = 3
        self.map = game_map

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
