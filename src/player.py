from car import Car
from lines import Lines

COLORS = {
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255)
}


class Player:
    def __init__(self, name, x, y, color_name):
        self.name = name
        self.car = Car(x, y, COLORS[color_name])
        self.lines = Lines(COLORS[color_name])

    def set_dest(self, v):
        self.car.move(v)
        self.lines.add(self.car.current_line)

    def get_next_pos(self):
        return self.car.get_next_pos()

    def draw(self, surf, main=False):
        self.car.draw(surf, main)
        self.lines.draw(surf)

    def __str__(self):
        return "%s - %s" %(self.name, self.car)
