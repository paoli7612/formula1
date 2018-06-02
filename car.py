from geom import Pos, Line, next_pos

class Car:
    def __init__(self, x, y, color):
        self.pos = Pos(x,y)
        self.last_pos = Pos(x,y)
        self.inPos = Pos(x,y)
        self.color = color

    def draw(self, surf, main=False):
        self.pos.draw(surf, main, self.color)

    def get_next_pos(self):
        return next_pos(self.last_pos, self.pos)

    def move(self, v):
        x,y = v
        p = self.get_next_pos()
        self.last_pos = self.pos.copy()
        self.pos = p.copy()
        self.pos.add(x, y)
        self.current_line = Line(self.last_pos, self.pos)

        if self.pos.isOut():
            print("out")
            self.pos = self.inPos.copy()
            self.last_pos = self.inPos.copy()

        self.inPos = self.pos.copy()

    def __str__(self):
        return "[%s] %s" %(str(self.color), self.pos)
