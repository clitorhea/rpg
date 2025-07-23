import pygame
import json
import os
from settings import TILE_SIZE

# Pygame init
pygame.init()
screen = pygame.display.set_mode((640, 480)) # Temporary size, will be updated after map load
pygame.display.set_caption("Lunewood Village")

# Load tilemap
with open("data/maps/lunewood_village.json") as f:
    tilemap_data = json.load(f)

map_width = tilemap_data['width']
map_height = tilemap_data['height']

screen_width = map_width * TILE_SIZE
screen_height = map_height * TILE_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))

# Load tileset
tileset_path = os.path.join("data", "maps", tilemap_data['tilesets'][0]['source'])
with open(tileset_path) as f:
    tileset_data = json.load(f)

first_gid = tilemap_data['tilesets'][0]['firstgid']
tile_images = {}

for tile_info in tileset_data['tiles']:
    image_path = os.path.join("assets", tile_info['image'])
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
    tile_images[first_gid + tile_info['id']] = image

# Load layers
layers = tilemap_data['layers']
tile_layers = [layer for layer in layers if layer['type'] == 'tilelayer']

# Render map
def draw_map():
    for layer in tile_layers:
        data = layer['data']
        for i, gid in enumerate(data):
            if gid > 0:
                x = (i % map_width) * TILE_SIZE
                y = (i // map_width) * TILE_SIZE
                screen.blit(tile_images[gid], (x, y))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_map()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
