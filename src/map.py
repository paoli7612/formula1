import pickle, os

class Map:
    def __init__(self, path_map):
        self.path = path_map
        self.data = dict()
        if not self.exist():
            self.save()

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return self.data.values.__iter__()

    def __str__(self):
        return str(self.data)

    def exist(self):
        return os.path.exists(self.path)

    def items(self):
        return self.data.items()

    def save(self):
        pickle.dump(self.data, open(self.path, "wb"))

    def load(self):
        with open(self.path, 'rb') as handle:
            b = pickle.load(handle)
