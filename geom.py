import pygame

import conf



class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset_t()

    def reset_t(self):
        self.t = (self.x*conf.TILE, self.y*conf.TILE)

    def draw(self, surf, main, color):
        pygame.draw.circle(surf, color, self.t, conf.RAD_POS + 5*main)

    def add(self, x, y):
        self.x += x-1
        self.y += y-1
        self.reset_t()

    def __str__(self):
        return "%d,%d" %(self.x, self.y)


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, surf):
        pygame.draw.line(surf, conf.COLOR_LINE, self.start.t, self.end.t)

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
