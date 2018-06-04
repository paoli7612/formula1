import pygame
from shapely.geometry import LineString

import conf
from intersection import getIntersectPoint as intersect

def next_pos(last, current):
    x = current.x*2 - last.x
    y = current.y*2 - last.y
    return Pos(x, y)

def newLine(p1,p2):
    "Line from 2 tuple"
    p1 = Pos(*p1)
    p2 = Pos(*p2)
    return Line(p1,p2)


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

    def copy(self):
        return Pos(self.x, self.y)

    def isOut(self):
        print(self.x, self.y)
        if self.x < 0 or self.y < 0 or self.x > conf.TILE_X or self.y > conf.TILE_Y:
            return True

    def __str__(self):
        return "%d,%d" %(self.x, self.y)


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def coords(self):
        return self.start.x, self.start.y, self.end.x, self.end.y

    def draw(self, surf, color):
        pygame.draw.line(surf, color, self.start.t, self.end.t, 5)

    def intersect(self, line):
        x1,y1,x2,y2 = self.coords()
        line1 = LineString([(x1,y1),(x2,y2)])
        x1,y1,x2,y2 = line.coords()
        line2 = LineString([(x1,y1),(x2,y2)])
        b = bool(line1.intersection(line2))
        return b
        
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
