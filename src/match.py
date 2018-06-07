import pygame

from window import Window
from dest import Dest
from event_handler import EventHandlerKey


class Match:
    def __init__(self, map, *players):
        self.window = Window()
        self.event_handler = EventHandlerKey()
        self.players = players
        self.map = map
        self.dest = Dest()
        self.server = None

    def set_server(self, server):
        self.server = server

    def draw(self):
        self.window.draw()
        self.map.draw(self.window.screen)
        for player in self.players:
            player.draw(self.window.screen)
        self.current_player.draw(self.window.screen, True)
        self.dest.draw(self.window.screen, self.current_player.get_next_pos())
        pygame.display.flip()
        if self.server:
            self.server.send_screen(self.window.screen)

    def start(self):
        if self.server:
            self.server.send_start()
        self.running = True
        self.turn = -1
        self.change_turn()
        self.draw()
        self.loop()
        if self.server:
            self.server.send_end()

    def change_turn(self):
        self.turn = (self.turn+1)%len(self.players)
        self.current_player = self.players[self.turn]

    def events(self):
        if self.server:
            v = self.server.get_event()
        else:
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
