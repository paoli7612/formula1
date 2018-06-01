import pygame

from geom import Pos
import conf

draw_line = pygame.draw.line
draw_circle = pygame.draw.circle

class Dest:
    def __init__(self, x, y):
        self.image = pygame.Surface(conf.DEST_SIZE)

        x = x-1.5
        y = y-1.5

        # grid
        self.image.fill(conf.COLOR_KEY)
        for n in range(0,conf.DEST_TILE+1,conf.TILE):
            draw_line(self.image, conf.COLOR_DEST, (n,0), (n,conf.DEST_TILE), 4)
            draw_line(self.image, conf.COLOR_DEST, (0,n), (conf.DEST_TILE,n), 4)
            for i in range(3):
                self.draw_cross(n+conf.TILE//2, i*conf.TILE+conf.TILE//2)
        self.image.set_colorkey(conf.COLOR_KEY)

        self.rect = self.image.get_rect()
        self.pos = Pos(x,y)
        self.rect.topleft = self.pos.t

    def draw_cross(self, x, y):
        draw_circle(self.image, conf.COLOR_POS, (x,y), conf.RAD_POS)

    def draw(self, surf):
        surf.blit(self.image, self.rect)

if __name__ == "__main__":
    # test
    s = pygame.display.set_mode(conf.SIZE)
    s.fill(conf.COLOR_BGROUND)
    d = Dest(10,10)
    d.draw(s)
    pygame.display.flip()

    import time
    time.sleep(2)
