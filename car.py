from geom import Pos, Line

class Car:
    def __init__(self, x, y, color):
        self.pos = Pos(x,y)
        self.last_pos = Pos(x,y)
        self.color = color

    def draw(self, surf, main=False):
        self.pos.draw(surf, main, self.color)

    def move(self, v):
        x,y = v
        print(x,y)
        self.last_pos = self.pos.copy()
        self.pos.add(x, y)
        self.current_line = Line(self.last_pos, self.pos)

    def __str__(self):
        return "[%s] %s" %(str(self.color), self.pos)
