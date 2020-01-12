import pygame, sys
from pygame.locals import *


class Unit:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

    def render(self, window);
        window.blit(self.sprite, (self.x, self.y))

    