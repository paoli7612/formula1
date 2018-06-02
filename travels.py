import pygame

import conf

class Travels:
    def __init__(self, color):
        self.screen = pygame.Surface(conf.SIZE)
        self.screen.fill(conf.COLOR_KEY)
        self.screen.set_colorkey(conf.COLOR_KEY)
        self.data = list()
        self.color = color

    def add(self, line):
        line.draw(self.screen, self.color)
        self.data.append(line)

    def draw(self, surf):
        surf.blit(self.screen, (0,0))
