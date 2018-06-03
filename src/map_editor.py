import os

from map import Map
from window import Window
from geom import newLine
from event_handler import EventHandlerMouse

class Map_editor:
    def __init__(self, name_map):
        self.window = Window()
        self.map = Map(name_map)
        self.event_handler = EventHandlerMouse()

        self.window.draw()
        self.map.draw(self.window.screen)
        self.window.flip()

        self.running = True
        while self.running:
            p1 = self.event_handler.start()
            if p1:
                p2 = self.event_handler.start()

            if not p1 or not p2:
                self.running = False
            else:
                line = newLine(p1,p2)

                self.map.add(line)
                self.map.draw(self.window.screen)

                self.window.flip()

        self.map.save()


if __name__ == "__main__":
    Map_editor("asd")
    import time
    time.sleep(1)
