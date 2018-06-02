import os

from map import Map
from window import Window
from geom import newLine

def main(name_map):
    path = os.path.dirname(__file__)
    path_map = os.path.join(path, "..", "maps", name_map)
    map = Map(path_map)
    map.add(newLine((12,16),(10,10)))

    window = Window()
    window.draw()
    map.draw(window.screen)
    window.flip()

    map.save()

if __name__ == "__main__":
    main("map1")
    import time
    time.sleep(1)
