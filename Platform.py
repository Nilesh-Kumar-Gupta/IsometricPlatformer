import pygame
from SpriteSheet import SpriteSheet

sprite_sheet = SpriteSheet("Assets/platformer_block.png", "Assets/platform_block.json")


class Platform(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Platform, self).__init__()

        self.surf = sprite_sheet.parse_sprite("platform_block.png")

        self.rect = self.surf.get_rect(center=(screen_width - 50, screen_height - 10))
