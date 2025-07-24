from src.asset_manager import ASSET_INFO
import pygame

def draw_map(surface, base_layer, object_layer, assets, camera_x, camera_y, npc_positions, tile_size):
    for y, (row_base, row_obj) in enumerate(zip(base_layer, object_layer)):
        for x, (base, obj) in enumerate(zip(row_base, row_obj)):
            # Draw base
            if base is not None:
                asset = assets[base]
                offset_x, offset_y = ASSET_INFO[base]["offset"]
                screen_x = x * tile_size - camera_x + offset_x
                screen_y = y * tile_size - camera_y + offset_y
                surface.blit(asset, (screen_x, screen_y))
            # Draw object (on top)
            if obj is not None:
                asset = assets[obj]
                offset_x, offset_y = ASSET_INFO[obj]["offset"]
                screen_x = x * tile_size - camera_x + offset_x
                screen_y = y * tile_size - camera_y + offset_y
                surface.blit(asset, (screen_x, screen_y))
    # Draw NPCs
    for nx, ny in npc_positions:
        screen_x = nx * tile_size - camera_x
        screen_y = ny * tile_size - camera_y
        pygame.draw.ellipse(surface, (255, 140, 0), (screen_x+2, screen_y+2, tile_size-4, tile_size-4))