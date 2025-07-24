import os
import pygame

ASSET_INFO = {
    "grass":  {"file": "assets/village/GRASS DETAIL 2 - DAY.png",  "size": (16, 16),   "offset": (0, 0)},
    "cobble": {"file": "assets/village/cobble.png",      "size": (16, 16),   "offset": (0, 0)},
    "ground": {"file": "assets/village/GROUND TILE - DAY.png", "size": (16, 16),   "offset": (0, 0)},
    "dirt":   {"file": "assets/village/GROUND DETAIL 2 - DAY",  "size": (16, 16),   "offset": (0, 0)},
    "water":  {"file": "assets/village/WATER TILE - DAY.png",  "size": (16, 16),   "offset": (0, 0)},
    "path":   {"file": "assets/village/path.png",   "size": (16, 16),   "offset": (0, 0)},
    "tree":   {"file": "assets/village/TREE 1 - DAY.png",   "size": (48, 48),   "offset": (0, -32)},
    "rock":   {"file": "assets/village/TERRAIN SET 4 - DAY",   "size": (48, 64),   "offset": (0, -48)},
    "house":  {"file": "assets/village/HOUSE 1 - DAY.png",  "size": (64, 64),   "offset": (0, -48)},
    "shop":   {"file": "assets/village/HOUSE 2 - DAY",   "size": (48, 48),   "offset": (0, -32)},
    "player": {"file": "assets/dungeon/player/base/demigod_m.png", "size": (16, 16),   "offset": (0, 0)},
    "shrine": {"file": "assets/village/shrine.png", "size": (16, 16),   "offset": (0, 0)},
    "plaza_tree": {"file": "assets/village/plaza_tree.png", "size": (16, 16),   "offset": (0, 0)},
    "aether_font": {"file": "assets/village/aether_font.png", "size": (16, 16),   "offset": (0, 0)},
    "stage": {"file": "assets/village/stage.png", "size": (16, 16),   "offset": (0, 0)},
    "bulletin": {"file": "assets/village/bulletin.png", "size": (16, 16),   "offset": (0, 0)},
    "market_stall": {"file": "assets/village/market_stall.png", "size": (16, 16),   "offset": (0, 0)},
    "lodge": {"file": "assets/village/lodge.png", "size": (16, 16),   "offset": (0, 0)},
    "forge": {"file": "assets/village/forge.png", "size": (16, 16),   "offset": (0, 0)},
    "inn": {"file": "assets/village/inn.png", "size": (16, 16),   "offset": (0, 0)},
    "mill": {"file": "assets/village/mill.png", "size": (16, 16),   "offset": (0, 0)},
    "dock": {"file": "assets/village/dock.png", "size": (16, 16),   "offset": (0, 0)},
    "ruin": {"file": "assets/village/ruin.png", "size": (16, 16),   "offset": (0, 0)},
    "field": {"file": "assets/village/field.png", "size": (16, 16),   "offset": (0, 0)},
    "fence": {"file": "assets/village/fence.png", "size": (16, 16),   "offset": (0, 0)}
}

def load_image_with_fallback(path, size, fallback_color):
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, size)
    else:
        surf = pygame.Surface(size, pygame.SRCALPHA)
        surf.fill(fallback_color)
        return surf

def get_assets():
    assets = {}
    for key, info in ASSET_INFO.items():
        fallback = (120, 120, 120) if key != "player" else (255, 220, 40)
        assets[key] = load_image_with_fallback(info["file"], info["size"], fallback)
    return assets