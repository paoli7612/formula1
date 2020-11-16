import pygame

import conf
from geom import newLine

KEYS = [
    [113,119,101],
    [97,115,100],
    [122,120,99]
]


class EventHandler:
    def run(self):
        self.clock = pygame.time.Clock()
        self.running = True
        while self.running:
            self.clock.tick(conf.FPS)
            for event in pygame.event.get():
                self.event(event)


class EventHandlerKey(EventHandler):
    def get_pos(self, key):
        for y,row in enumerate(KEYS):
            for x,n in enumerate(row):
                if key == n: return (x,y)

    def event(self,event):
        if event.type == pygame.QUIT:
            self.running = False
            self.last_action = "quit"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.last_action = "quit"
            else: self.last_action = self.get_pos(event.key)
            self.running = False

    def start(self):
        self.running = True
        self.run()
        return self.last_action

class EventHandlerMouse(EventHandler):
    def event(self, event):
        # MOUSEMOTION
        if event.type == pygame.MOUSEMOTION:

            x,y = event.pos
            x = x//conf.TILE * conf.TILE
            y = y//conf.TILE * conf.TILE
            self.last_pos = (x,y)

            last_screen = self.screen.copy()
            pygame.draw.circle(self.screen,(255,255,0),(x,y),5)
            pygame.display.flip()
            self.screen.blit(last_screen, (0,0))

        # MOUSEBUTTONDOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.last_pos:
                x,y = self.last_pos
                pygame.draw.circle(self.screen,(255,255,0),(x,y),5)
                x /= conf.TILE
                y /= conf.TILE
                self.last_pos = (x,y)
                self.running = False

        # QUIT
        if event.type == pygame.QUIT:
            self.last_pos = False
            self.running = False


    def start(self):
        self.running = True
        self.last_pos = False
        self.screen = pygame.display.get_surface()
        last_screen = self.screen.copy()
        self.run()
        p1 = self.last_pos
        if p1:
            self.run()
            p2 = self.last_pos
            if p2:
                self.screen.blit(last_screen,(0,0))
                return newLine(p1,p2)
