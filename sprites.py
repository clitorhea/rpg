# sprites.py

import pygame
import math
from settings import TILE_SIZE, WHITE, RED, BROWN, PLAYER_IMG, ENEMY_IMG, WALL_IMG, PLAYER_ANIMATIONS, ENEMY_ANIMATIONS, ANIMATION_SPEED

# Wall Class
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(WALL_IMG).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = self._load_animations(PLAYER_ANIMATIONS)
        self.current_animation = 'idle_down' # Default animation
        self.current_frame = 0
        self.last_frame_update = pygame.time.get_ticks()
        self.image = self.animations[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.attacking = False
        self.attack_time = 0
        self.attack_duration = 200  # milliseconds
        self.health = 100
        self.max_health = 100
        self.attack_damage = 10
        self.direction = 'down' # Default direction
        self.last_moved_direction = 'down' # Store the last direction moved for idle animation

    def _load_animations(self, anim_dict):
        animations = {}
        for state, paths in anim_dict.items():
            frames = []
            for path in paths:
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, (TILE_SIZE - 10, TILE_SIZE - 10))
                frames.append(img)
            animations[state] = frames
        return animations

    def set_animation_state(self, new_state):
        if self.current_animation != new_state:
            self.current_animation = new_state
            self.current_frame = 0
            self.last_frame_update = pygame.time.get_ticks()

    def update(self, keys, enemies, walls):
        # Movement
        dx = 0
        dy = 0
        moving = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
            self.direction = 'left'
            moving = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
            self.direction = 'right'
            moving = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
            self.direction = 'up'
            moving = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed
            self.direction = 'down'
            moving = True

        # Set animation based on movement and direction
        if moving:
            self.set_animation_state(f'walk_{self.direction}')
            self.last_moved_direction = self.direction
        else:
            self.set_animation_state(f'idle_{self.last_moved_direction}') # Use last_moved_direction for idle

        # Update animation frame
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_update > ANIMATION_SPEED:
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.current_frame]
            self.last_frame_update = current_time
            
            # Flip image if direction is left and no specific left animation is provided
            if self.direction == 'left' and '_left' not in self.current_animation:
                self.image = pygame.transform.flip(self.image, True, False)


        # Move and collide
        self.rect.x += dx
        collided_walls = pygame.sprite.spritecollide(self, walls, False)
        for wall in collided_walls:
            if dx > 0:
                self.rect.right = wall.rect.left
            elif dx < 0:
                self.rect.left = wall.rect.right

        self.rect.y += dy
        collided_walls = pygame.sprite.spritecollide(self, walls, False)
        for wall in collided_walls:
            if dy > 0:
                self.rect.bottom = wall.rect.top
            elif dy < 0:
                self.rect.top = wall.rect.bottom

        # Attack timer
        if self.attacking:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time > self.attack_duration:
                self.attacking = False

    def attack(self, enemies):
        if not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            
            # Create hitbox based on direction
            if self.direction == 'right':
                attack_rect = pygame.Rect(self.rect.right, self.rect.y, TILE_SIZE, self.rect.height)
            elif self.direction == 'left':
                attack_rect = pygame.Rect(self.rect.left - TILE_SIZE, self.rect.y, TILE_SIZE, self.rect.height)
            elif self.direction == 'down':
                attack_rect = pygame.Rect(self.rect.x, self.rect.bottom, self.rect.width, TILE_SIZE)
            elif self.direction == 'up':
                attack_rect = pygame.Rect(self.rect.x, self.rect.top - TILE_SIZE, self.rect.width, TILE_SIZE)

            for enemy in enemies:
                if attack_rect.colliderect(enemy.rect):
                    enemy.take_damage(self.attack_damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill() # Player dies

# Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animations = self._load_animations(ENEMY_ANIMATIONS)
        self.current_animation = 'idle_down' # Default animation
        self.current_frame = 0
        self.last_frame_update = pygame.time.get_ticks()
        self.image = self.animations[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2
        self.health = 50
        self.max_health = 50
        self.attack_damage = 5
        self.aggro_radius = 200
        self.direction = 'down' # Default direction
        self.last_moved_direction = 'down' # Store the last direction moved for idle animation

    def _load_animations(self, anim_dict):
        animations = {}
        for state, paths in anim_dict.items():
            frames = []
            for path in paths:
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, (TILE_SIZE - 10, TILE_SIZE - 10))
                frames.append(img)
            animations[state] = frames
        return animations

    def set_animation_state(self, new_state):
        if self.current_animation != new_state:
            self.current_animation = new_state
            self.current_frame = 0
            self.last_frame_update = pygame.time.get_ticks()

    def update(self, player, walls):
        # Simple AI: move towards player if within aggro radius
        distance_to_player = math.hypot(self.rect.centerx - player.rect.centerx, self.rect.centery - player.rect.centery)

        dx = 0
        dy = 0
        moving = False

        if distance_to_player < self.aggro_radius:
            # Move towards player
            p_dx = player.rect.centerx - self.rect.centerx
            p_dy = player.rect.centery - self.rect.centery
            dist = math.hypot(p_dx, p_dy)
            if dist > 0:
                dx = p_dx / dist * self.speed
                dy = p_dy / dist * self.speed
                moving = True
                if abs(p_dx) > abs(p_dy): # Prioritize horizontal movement for direction
                    if p_dx > 0:
                        self.direction = 'right'
                    else:
                        self.direction = 'left'
                else: # Prioritize vertical movement for direction
                    if p_dy > 0:
                        self.direction = 'down'
                    else:
                        self.direction = 'up'
        
        if moving:
            self.set_animation_state(f'walk_{self.direction}')
            self.last_moved_direction = self.direction
        else:
            self.set_animation_state(f'idle_{self.last_moved_direction}')

        # Update animation frame
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_update > ANIMATION_SPEED:
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.current_frame]
            self.last_frame_update = current_time

            # Flip image if direction is left and no specific left animation is provided
            if self.direction == 'left' and '_left' not in self.current_animation:
                self.image = pygame.transform.flip(self.image, True, False)

        # Move and collide
        self.rect.x += dx
        collided_walls = pygame.sprite.spritecollide(self, walls, False)
        for wall in collided_walls:
            if dx > 0:
                self.rect.right = wall.rect.left
            elif dx < 0:
                self.rect.left = wall.rect.right

        self.rect.y += dy
        collided_walls = pygame.sprite.spritecollide(self, walls, False)
        for wall in collided_walls:
            if dy > 0:
                self.rect.bottom = wall.rect.top
            elif dy < 0:
                self.rect.top = wall.rect.bottom

        # Check for collision with player
        if self.rect.colliderect(player.rect):
            player.take_damage(self.attack_damage)


    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
