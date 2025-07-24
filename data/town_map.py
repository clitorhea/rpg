# Map size: 50x50 for demo
SIZE = 50

# BASE_LAYER: grass everywhere, river (water) at south, plaza (cobble) at center
BASE_LAYER = [["grass" for _ in range(SIZE)] for _ in range(SIZE)]

# Plaza (~8x8) with cobble at center
for y in range(21, 29):
    for x in range(21, 29):
        BASE_LAYER[y][x] = "cobble"

# Paths radiating from plaza
for y in range(0, SIZE):
    BASE_LAYER[y][25] = "dirt"  # vertical path
for x in range(0, SIZE):
    BASE_LAYER[25][x] = "dirt"  # horizontal path

# River (water) at the bottom
for x in range(SIZE):
    for y in range(SIZE-5, SIZE):
        BASE_LAYER[y][x] = "water"

# Fields/farmland at west
for y in range(30, 37):
    for x in range(7, 17):
        BASE_LAYER[y][x] = "dirt"

# OBJECT_LAYER: all None by default
OBJECT_LAYER = [[None for _ in range(SIZE)] for _ in range(SIZE)]

# Dense woods at borders (north, east, west)
for i in range(SIZE):
    for j in range(0, 4):
        OBJECT_LAYER[j][i] = "tree"           # North
        OBJECT_LAYER[i][j] = "tree"           # West
        OBJECT_LAYER[i][SIZE-1-j] = "tree"    # East

# Plaza: Song-Oak at center, aether font, market stalls, stage, bulletin
OBJECT_LAYER[25][25] = "plaza_tree"
OBJECT_LAYER[26][25] = "aether_font"
OBJECT_LAYER[23][25] = "stage"
OBJECT_LAYER[25][22] = "bulletin"
for x in range(23, 28):
    OBJECT_LAYER[28][x] = "market_stall"

# Player's house (NW)
for y in range(15, 18):
    for x in range(10, 13):
        OBJECT_LAYER[y][x] = "house"

# Elder's Lodge (NE)
for y in range(15, 18):
    for x in range(37, 41):
        OBJECT_LAYER[y][x] = "lodge"

# Blacksmith (E)
for y in range(26, 29):
    for x in range(38, 41):
        OBJECT_LAYER[y][x] = "forge"

# Inn (E, next to blacksmith)
for y in range(30, 33):
    for x in range(38, 41):
        OBJECT_LAYER[y][x] = "inn"

# Farmsteads (W)
for y in range(34, 37):
    for x in range(10, 13):
        OBJECT_LAYER[y][x] = "house"

# Mill and dock (S)
for x in range(20, 24):
    for y in range(SIZE-8, SIZE-5):
        OBJECT_LAYER[y][x] = "mill"
for x in range(27, 30):
    for y in range(SIZE-8, SIZE-5):
        OBJECT_LAYER[y][x] = "dock"

# Echoing Grove (Ruin, N)
for y in range(7, 10):
    for x in range(22, 27):
        OBJECT_LAYER[y][x] = "ruin"

# Hidden Glade (NW, shrine)
OBJECT_LAYER[6][7] = "shrine"

# Fields (W)
for y in range(37, 41):
    for x in range(7, 17):
        OBJECT_LAYER[y][x] = "field"

# Scatter rocks, fences, trees in the forest
import random
for _ in range(80):
    x, y = random.randint(4, SIZE-5), random.randint(4, 20)
    if OBJECT_LAYER[y][x] is None:
        OBJECT_LAYER[y][x] = random.choice(["rock", "tree"])
for _ in range(40):
    x, y = random.randint(4, 46), random.randint(30, 46)
    if OBJECT_LAYER[y][x] is None:
        OBJECT_LAYER[y][x] = "fence"

# NPCs: in plaza, inn, forge, player's house, farm, etc.
NPC_POSITIONS = [
    (25, 25),  # Plaza (singing under Song-Oak)
    (24, 27),  # Plaza
    (22, 25),  # Plaza
    (39, 27),  # Blacksmith
    (39, 31),  # Inn
    (11, 16),  # Player house
    (12, 35),  # Farmstead
    (7, 7),    # Hidden glade
    (24, SIZE-7),  # Mill
]

# You can add more details, secret paths, or environmental decorations as needed.