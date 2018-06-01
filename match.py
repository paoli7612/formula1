import pygame

from window import Window
from dest import Dest
from event_handler import EventHandler


class Match:
    def __init__(self, *players):
        self.window = Window()
        self.event_handler = EventHandler()
        self.players = players
        d = Dest(5, 7)

    def start(self):
        self.running = True
        self.window.draw()
        for player in self.players:
            player.draw(self.window.screen)
        pygame.display.flip()

    def loop(self):
        while self.running:
            v = e.run()
            if v == "quit":
                running = False
            else:
                if v: print(v)
