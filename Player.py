import pygame.sprite
from SpriteSheet import SpriteSheet

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

sprite_sheet_image = pygame.image.load(
    "Assets/mystic_woods_free_v0.2/sprites/characters/player.png"
)
sprite_sheet = SpriteSheet(sprite_sheet_image)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        self.surf = sprite_sheet.get_image(0, 50, 50, 2, (135, 206, 250))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys, screen_width, screen_height):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # check whether player exceeds window horizontal
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

        # check whether player exceeds window vertical
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
