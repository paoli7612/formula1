from geom import Pos

class Car:
    def __init__(self, x, y):
        self.pos = Pos(x,y)
        self.last_pos = Pos(x,y)
        self.color = "red"

    def draw(self, surf):
        self.pos.draw(surf)

    def __str__(self):
        return "[%s] %s" %(self.color, self.pos)
