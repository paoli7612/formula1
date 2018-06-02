import pygame

from window import Window
from dest import Dest
from event_handler import EventHandlerKey


class Match:
    def __init__(self, *players):
        self.window = Window()
        self.event_handler = EventHandlerKey()
        self.players = players
        self.d = Dest()

    def draw(self):
        self.window.draw()
        for player in self.players:
            player.draw(self.window.screen)
        self.current_player.draw(self.window.screen, True)
        self.d.draw(self.window.screen, self.current_player.get_next_pos())
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
        v = self.event_handler.start()
        if v == "quit":
            self.running = False
        self.last_choice = v

    def update(self):
        if self.last_choice and not self.last_choice == "quit":
            self.current_player.set_dest(self.last_choice)
            self.change_turn()

    def loop(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
