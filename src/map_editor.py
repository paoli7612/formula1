import os

from map import Map
from window import Window

def main(name_map):
    path = os.path.dirname(__file__)
    path_map = os.path.join(path, "..", "maps", name_map)
    map = Map(path_map)

    window = Window()
    window.draw()
    map.draw(window.screen)


if __name__ == "__main__":
    main("map1")
    import time
    time.sleep(1)
