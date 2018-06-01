import pygame
COLOR_LINE = (0,255,180)
COLOR_POS = (255,255,0)

RAD_POS = 4

draw_line = pygame.draw.line
draw_circle = pygame.draw.circle

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = (x,y)

    def draw(self, surf):
        draw_circle(surf, COLOR_POS, self.t, RAD_POS)


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, surf):
        draw_line(surf, COLOR_LINE, self.start.t, self.end.t)




if __name__ == "__main__":
    # test
    s = pygame.display.set_mode((400,400))
    p = Pos(10,10)
    p.draw(s)
    p1 = Pos(40,40)
    l = Line(p,p1)
    l.draw(s)

    pygame.display.flip()
    import time
    time.sleep(2)
