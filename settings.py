import pygame
from sys import exit

# Constants for screen and tile size
TILE_SIZE = 40     # Each tile is 40x40 pixels
GRID_WIDTH, GRID_HEIGHT = 10, 10
SCREEN_WIDTH = TILE_SIZE * GRID_WIDTH
SCREEN_HEIGHT = TILE_SIZE * GRID_HEIGHT

# Map data (same as before)
map_data = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 3, 1, 0, 1, 3, 1, 6, 2],
    [2, 1, 0, 1, 0, 4, 1, 1, 1, 2],
    [2, 1, 3, 1, 0, 4, 1, 5, 1, 2],
    [2, 1, 0, 1, 0, 0, 0, 1, 3, 2],
    [2, 4, 0, 1, 4, 0, 1, 1, 1, 2],
    [2, 1, 0, 1, 0, 0, 1, 3, 6, 2],
    [2, 1, 3, 1, 0, 4, 1, 0, 0, 2],
    [2, 1, 1, 1, 0, 1, 3, 1, 4, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

# Tileset: map codes to emoji or symbols
tileset = {
    0: "▫️",   # Dirt path (Ground)
    1: "🌱",   # Grass
    2: "💧",   # Water tile (unwalkable)
    3: "🌲",   # Tree
    4: "🏠",   # Building
    5: "🪨",   # Rock/ore deposit
    6: "建篡",  # Fence
}

# Player settings
player_char = "@"
initial_x, initial_y = 4, 4  # Start at the center of a dirt path

def draw_grid(screen, map_data, player_pos):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            tile_code = map_data[y][x]
            tile_surface = pygame.font.SysFont(None, TILE_SIZE).render(tileset[tile_code], True, (255, 255, 255))
            screen.blit(tile_surface, (x * TILE_SIZE, y * TILE_SIZE))

    # Draw player
    px, py = player_pos
    msg = pygame.font.SysFont(None, TILE_SIZE).render(player_char, True, (0, 255, 0))
    screen.blit(msg, (px * TILE_SIZE, py * TILE_SIZE))

def is_valid_tile(x, y):
    return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT and map_data[y][x] != 2

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stardew Valley Map Explorer")

clock = pygame.time.Clock()

player_pos = [initial_x, initial_y]

running = True
while running:
    screen.fill((0, 0, 0))  # Black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    new_pos = player_pos.copy()

    if keys[pygame.K_w]:
        new_pos[1] -= 1
    elif keys[pygame.K_s]:
        new_pos[1] += 1
    elif keys[pygame.K_a]:
        new_pos[0] -= 1
    elif keys[pygame.K_d]:
        new_pos[0] += 1

    if is_valid_tile(new_pos[0], new_pos[1]):
        player_pos = new_pos

    draw_grid(screen, map_data, player_pos)

    pygame.display.flip()
    clock.tick(60)  # Cap at 60 FPS

pygame.quit()
exit()
