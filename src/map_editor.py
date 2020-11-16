import os, sys

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
            line = self.event_handler.start()
            if line:
                self.map.add(line)
                self.map.draw(self.window.screen)
                self.window.flip()
            else:
                self.running = False

        if input('save?(Si/No)') == 'Si':
            self.map.save()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        Map_editor(sys.argv[1])
    else:
        print("add map name as argument")
