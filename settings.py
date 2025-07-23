# settings.py

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
DARK_GREEN = (0, 100, 0)

# Tile settings
TILE_SIZE = 32

# Asset Paths
PLAYER_IMG = "assets/player/base/human_m.png"
ENEMY_IMG = "assets/dc-mon/goblin.png"
WALL_IMG = "assets/dc-dngn/wall/brick_brown0.png"
FLOOR_IMG = "assets/dc-dngn/floor/dirt0.png"

# Animation settings
ANIMATION_SPEED = 100 # Milliseconds per frame

# Player Animation Paths (placeholders for now)
PLAYER_ANIMATIONS = {
    'idle_right': [PLAYER_IMG],
    'idle_left': [PLAYER_IMG],
    'idle_up': [PLAYER_IMG],
    'idle_down': [PLAYER_IMG],
    'walk_right': [PLAYER_IMG],
    'walk_left': [PLAYER_IMG],
    'walk_up': [PLAYER_IMG],
    'walk_down': [PLAYER_IMG],
}

# Enemy Animation Paths (placeholders for now)
ENEMY_ANIMATIONS = {
    'idle_right': [ENEMY_IMG],
    'idle_left': [ENEMY_IMG],
    'idle_up': [ENEMY_IMG],
    'idle_down': [ENEMY_IMG],
    'walk_right': [ENEMY_IMG],
    'walk_left': [ENEMY_IMG],
    'walk_up': [ENEMY_IMG],
    'walk_down': [ENEMY_IMG],
}
