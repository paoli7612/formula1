from car import Car

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.car = Car(x, y)

    def __str__(self):
        return "%s - %s" %(self.name, self.car)
