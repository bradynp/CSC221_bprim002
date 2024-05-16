from random import randint

import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.left = self.screen.get_rect().right
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.alien_speed
        self.rect.x = self.x