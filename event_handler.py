import pygame

import conf

class EventHandler:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.last_action = None

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.last_action = "quit"
            if event.type == pygame.KEYDOWN:
                self.last_action = event.key
                self.running = False

    def loop(self):
        while self.running:
            self.clock.tick(conf.FPS)
            self.events()

    def run(self):
        self.loop()
        return self.last_action
