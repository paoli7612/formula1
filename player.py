from car import Car

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.car = Car(x, y)
