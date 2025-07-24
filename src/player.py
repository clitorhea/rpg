import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, assets, tile_size):
        super().__init__()
        self.image = assets["player"]
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2
        self.tile_size = tile_size

    def move(self, dx, dy, base_layer, object_layer, npc_positions, solid_objects, tile_size):
        new_rect = self.rect.move(dx, dy)
        min_tile_x = new_rect.left // tile_size
        min_tile_y = new_rect.top // tile_size
        max_tile_x = (new_rect.right - 1) // tile_size + 1
        max_tile_y = (new_rect.bottom - 1) // tile_size + 1

        for y in range(min_tile_y, max_tile_y):
            for x in range(min_tile_x, max_tile_x):
                if 0 <= x < len(base_layer[0]) and 0 <= y < len(base_layer):
                    if (object_layer[y][x] in solid_objects) or ((x, y) in npc_positions):
                        return
        self.rect = new_rect