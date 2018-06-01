from car import Car

COLORS = {
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255)
}


class Player:
    def __init__(self, name, x, y, color_name):
        self.name = name
        self.car = Car(x, y, COLORS[color_name])

    def draw(self, surf, main=False):
        self.car.draw(surf, main)

    def __str__(self):
        return "%s - %s" %(self.name, self.car)
