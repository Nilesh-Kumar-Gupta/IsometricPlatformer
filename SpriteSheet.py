import pygame
import json


class SpriteSheet:
    def __init__(self, filename, metadata):
        self.filename = filename
        self.metadata = metadata

        # load spritesheet
        self.sprite_sheet = pygame.image.load(self.filename)

        # load metadata
        with open(self.metadata) as f:
            self.data = json.load(f)

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))

        # the transparent pixels are rendered as black, so this does not compute those black pixels
        # this only applies to value that are exactly (0, 0, 0) so any other values would not be ignored
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data["frames"][name]["frame"]
        return self.get_sprite(sprite["x"], sprite["y"], sprite["w"], sprite["h"])
