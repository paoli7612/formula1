import os

from map import Map
from window import Window

class Boss:
    def __init__(self, name_map):
        self.path = os.path.dirname(__file__)
        path_map = os.path.join(self.path, "..", "maps", name_map)
        self.map = Map(path_map)

        self.window = Window()
        self.window.draw()
        self.map.draw(self.window.screen)


if __name__ == "__main__":
    b = Boss("map1")
    import time
    time.sleep(1)
