import pygame.sprite
from SpriteSheet import SpriteSheet

from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

sprite_sheet = SpriteSheet("Assets/trainer_sheet.png", "Assets/trainer_sheet.json")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        # load the image into a list
        self.sprites = [
            sprite_sheet.parse_sprite(f"trainer{i + 1}.png") for i in range(0, 5)
        ]

        # rescale the image
        # self.surf = pygame.transform.scale(self.surf, (70, 70))

        # get index of current image
        self.index = 0

        self.surf = self.sprites[self.index]
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys, screen_width, screen_height):
        if pressed_keys[K_UP]:
            self.index = int((self.index + 1) % 5)
            self.surf = self.sprites[self.index]
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.index = int((self.index + 1) % 5)
            self.surf = self.sprites[self.index]
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.index = int((self.index + 1) % 5)
            self.surf = self.sprites[self.index]
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.index = int((self.index + 1) % 5)
            self.surf = self.sprites[self.index]
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
