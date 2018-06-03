import pickle, os

import conf
from lines import Lines

class Map:
    def __init__(self, name_map):
        path = os.path.dirname(__file__)
        path_folder = os.path.join(path, "..", "maps")
        path_map = os.path.join(path_folder, name_map)
        self.path = path_map
        self.lines = Lines(conf.COLOR_CONTOURN)
        if self.exist():
            self.load()
        else:
            self.save()

    def add(self, line):
        self.lines.add(line)

    def __str__(self):
        return str(self.lines)

    def draw(self, surf):
        self.lines.draw(surf)

    def exist(self):
        return os.path.exists(self.path)

    def items(self):
        return self.data.items()

    def save(self):
        pickle.dump(self.lines.data, open(self.path, "wb"))

    def load(self):
        with open(self.path, 'rb') as handle:
            data = pickle.load(handle)
        self.lines.reload(data)
