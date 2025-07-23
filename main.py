import pygame
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, WHITE, RED, GREEN, BROWN, DARK_GREEN, MAP, FLOOR_IMG
from sprites import Wall, Player, Enemy

# Initialize Pygame
pygame.init()

# Screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
DARK_GREEN = (0, 100, 0)

# Font
font = pygame.font.Font(None, 36)

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
walls = pygame.sprite.Group()

grass_tile = pygame.image.load(FLOOR_IMG).convert()
grass_tile = pygame.transform.scale(grass_tile, (TILE_SIZE, TILE_SIZE))

# Create walls and player/enemy based on map
for row_index, row in enumerate(MAP):
    for col_index, tile in enumerate(row):
        if tile == 1:
            wall = Wall(col_index * TILE_SIZE, row_index * TILE_SIZE)
            all_sprites.add(wall)
            walls.add(wall)

player = Player(100, 100)
all_sprites.add(player)

enemy1 = Enemy(300, 300)
all_sprites.add(enemy1)
enemies.add(enemy1)


# UI Function
def draw_ui(player, enemies):
    # Player health bar
    pygame.draw.rect(screen, RED, (10, 10, player.max_health * 2, 20))
    pygame.draw.rect(screen, GREEN, (10, 10, player.health * 2, 20))
    player_health_text = font.render(f"Player HP: {player.health}/{player.max_health}", True, WHITE)
    screen.blit(player_health_text, (10, 40))

    # Enemy health bars
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy.rect.x, enemy.rect.y - 20, enemy.max_health, 10))
        pygame.draw.rect(screen, GREEN, (enemy.rect.x, enemy.rect.y - 20, enemy.health, 10))


# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.attack(enemies)

    # Update
    keys = pygame.key.get_pressed()
    player.update(keys, enemies, walls)
    enemies.update(player, walls)


    # Draw
    # Draw grass background
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            screen.blit(grass_tile, (x, y))

    all_sprites.draw(screen)

    # Draw attack hitbox for visual feedback
    if player.attacking:
        if player.direction == 'right':
            attack_rect = pygame.Rect(player.rect.right, player.rect.y, TILE_SIZE, player.rect.height)
        elif player.direction == 'left':
            attack_rect = pygame.Rect(player.rect.left - TILE_SIZE, player.rect.y, TILE_SIZE, player.rect.height)
        elif player.direction == 'down':
            attack_rect = pygame.Rect(player.rect.x, player.rect.bottom, player.rect.width, TILE_SIZE)
        elif player.direction == 'up':
            attack_rect = pygame.Rect(player.rect.x, player.rect.top - TILE_SIZE, player.rect.width, TILE_SIZE)
        pygame.draw.rect(screen, WHITE, attack_rect, 2) # Draw outline

    # Draw UI
    draw_ui(player, enemies)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()