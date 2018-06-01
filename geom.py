import pygame

import conf

draw_line = pygame.draw.line
draw_circle = pygame.draw.circle

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = (x*conf.TILE, y*conf.TILE)

    def draw(self, surf):
        draw_circle(surf, conf.COLOR_POS, self.t, conf.RAD_POS)


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, surf):
        draw_line(surf, conf.COLOR_LINE, self.start.t, self.end.t)

if __name__ == "__main__":
    # test
    s = pygame.display.set_mode(conf.SIZE)
    p = Pos(10,10)
    p.draw(s)
    p1 = Pos(12,12)
    l = Line(p,p1)
    l.draw(s)

    pygame.display.flip()
    import time
    time.sleep(2)
