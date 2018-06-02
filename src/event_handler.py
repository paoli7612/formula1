import pygame

import conf

KEYS = [
    [113,119,101],
    [97,115,100],
    [122,120,99]
]


class EventHandler:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.last_action = None
        

    def get_pos(self, key):
        for y,row in enumerate(KEYS):
            for x,n in enumerate(row):
                if key == n: return (x,y)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.last_action = "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.last_action = "quit"
                else: self.last_action = self.get_pos(event.key)
                self.running = False

    def loop(self):
        while self.running:
            self.clock.tick(conf.FPS)
            self.events()

    def run(self):
        self.running = True
        self.loop()
        return self.last_action
