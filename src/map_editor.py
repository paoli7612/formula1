import os
from map import Map

class Boss:
    def __init__(self, name_map):
        self.path = os.path.dirname(__file__)
        path_map = os.path.join(self.path, "..", "maps", name_map)

        self.map = Map(path_map)
        self.map.load()
        print(self.map)
        self.map.save()


if __name__ == "__main__":
    b = Boss("map1")
