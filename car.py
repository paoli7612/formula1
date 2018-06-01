from geom import Pos

class Car:
    def __init__(self, x, y):
        self.pos = Pos(x,y)
        self.last_pos = Pos(x,y)
