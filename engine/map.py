import json
import pygame
import os

TILE_SIZE = 32

class Map:
    def __init__(self, map_file):
        with open(map_file) as f:
            data = json.load(f)

        self.tileset = pygame.image.load(data['tileset']).convert_alpha()
        self.layers = data['layers']
        self.tilemap = data['tilemap']
        self.width = data['width']
        self.height = data['height']

    def draw(self, screen, player):
        for layer in self.layers:
            for y in range(self.height):
                for x in range(self.width):
                    tile_id = self.tilemap[layer][y][x]
                    if tile_id == -1:
                        continue
                    tx = (tile_id % 8) * TILE_SIZE
                    ty = (tile_id // 8) * TILE_SIZE
                    screen.blit(self.tileset, (x * TILE_SIZE, y * TILE_SIZE),
                                (tx, ty, TILE_SIZE, TILE_SIZE))
