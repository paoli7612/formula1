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

    def draw(self):
        self.window.draw()
        for player in self.players:
            player.draw(self.window.screen)
        self.current_player.draw(self.window.screen, True)
        pygame.display.flip()

    def start(self):
        self.running = True
        self.turn = -1
        self.change_turn()
        self.draw()
        self.loop()

    def change_turn(self):
        self.turn = (self.turn+1)%len(self.players)
        self.current_player = self.players[self.turn]

    def events(self):
        v = self.event_handler.run()
        if v == "quit":
            self.running = False
            return
        if v:
            print(v,self.turn)
            self.change_turn()
            self.draw()
            pygame.display.flip()

    def loop(self):
        while self.running:
            self.events()