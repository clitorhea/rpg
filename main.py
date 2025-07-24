import pygame
import sys

from src.asset_manager import get_assets, ASSET_INFO
from src.player import Player
from src.game_map import draw_map
from data.town_map import BASE_LAYER, OBJECT_LAYER, NPC_POSITIONS

# === SETTINGS ===
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 16
# Define which object names are solid (for collision)
SOLID_OBJECTS = {"tree", "house", "rock", "shop", "lodge", "forge", "inn", "mill", "ruin", "shrine"}

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Stardew-like Village")
    clock = pygame.time.Clock()

    assets = get_assets()
    # Player starts at (3,3) tile, adjusts based on TILE_SIZE
    player = Player((TILE_SIZE * 5, TILE_SIZE * 5), assets, TILE_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_w]: dy -= player.speed
        if keys[pygame.K_s]: dy += player.speed
        if keys[pygame.K_a]: dx -= player.speed
        if keys[pygame.K_d]: dx += player.speed

        if dx != 0 or dy != 0:
            # Pass both layers and solid objects to the move function
            if dx != 0:
                player.move(dx, 0, BASE_LAYER, OBJECT_LAYER, NPC_POSITIONS, SOLID_OBJECTS, TILE_SIZE)
            if dy != 0:
                player.move(0, dy, BASE_LAYER, OBJECT_LAYER, NPC_POSITIONS, SOLID_OBJECTS, TILE_SIZE)

        # Camera follows player
        camera_x = player.rect.centerx - SCREEN_WIDTH // 2
        camera_y = player.rect.centery - SCREEN_HEIGHT // 2
        camera_x = max(0, min(camera_x, len(BASE_LAYER[0]) * TILE_SIZE - SCREEN_WIDTH))
        camera_y = max(0, min(camera_y, len(BASE_LAYER) * TILE_SIZE - SCREEN_HEIGHT))

        screen.fill((0, 0, 0))
        draw_map(
            screen,
            BASE_LAYER,
            OBJECT_LAYER,
            assets,
            camera_x,
            camera_y,
            NPC_POSITIONS,
            TILE_SIZE
        )
        # Draw player on top of layers
        screen.blit(assets["player"], (player.rect.x - camera_x, player.rect.y - camera_y))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()