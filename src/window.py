import pygame

import conf
from dest import Dest

class Window:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(conf.SIZE)
        pygame.display.set_caption(conf.TITLE)

        # grid
        self.grid = pygame.Surface(conf.SIZE)
        self.grid.fill(conf.COLOR_KEY)
        for x in range(0,conf.WIDTH+1,conf.TILE):
            pygame.draw.line(self.grid,conf.COLOR_GRID,(x,0),(x,conf.HEIGHT),3)
        for y in range(0,conf.HEIGHT+1,conf.TILE):
            pygame.draw.line(self.grid,conf.COLOR_GRID,(0,y),(conf.WIDTH,y),3)
        self.grid.set_colorkey(conf.COLOR_KEY)

    def draw(self):
        self.screen.fill(conf.COLOR_BGROUND)
        self.screen.blit(self.grid, (0,0))
        pygame.display.flip()

    def flip(self):
        pygame.display.flip()

if __name__ == "__main__":
    # test
    w = Window()
    w.draw()
    d = Dest(5,5)
    d.draw(w.screen)
    pygame.display.flip()


    import time
    time.sleep(2)
