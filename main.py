import pygame
from Player import Player
from Enemy import Enemy

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Define Screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# defining custom events
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)

# initializing player
player = Player()

# initializing sprite groups
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# define framerate
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADD_ENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # update player based on key press
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, SCREEN_WIDTH, SCREEN_HEIGHT)

    # update enemy
    enemies.update()

    screen.fill((135, 206, 250))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check for collision with enemies
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    pygame.display.flip()
    clock.tick(30)
