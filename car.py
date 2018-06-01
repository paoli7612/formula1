from geom import Pos

class Car:
    def __init__(self, x, y, color):
        self.pos = Pos(x,y)
        self.last_pos = Pos(x,y)
        self.color = color

    def draw(self, surf, main=False):
        self.pos.draw(surf, main, self.color)

    def __str__(self):
        return "[%s] %s" %(str(self.color), self.pos)
