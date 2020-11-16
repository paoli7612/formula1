from player import Player
from match import Match
from map import Map
from server import Server

def main(map_name, *players):
    map = Map(map_name)
    pp = list()
    for name, x, y, color in players:
        pp.append(Player(name, x, y, color, map))
    m = Match(map, *pp)
    m.start()

def server():
    s = Server()
    map = Map("map1")
    p1 = Player("nome1", 3, 1, "red", map)
    m = Match(map, p1)
    m.set_server(s)
    m.start()

def client():
    c = Client()
    c.run()

if __name__ == "__main__":
    main("map1", ('name1', 3, 1, 'blue'), ('name2', 6, 1, 'red'), ('name3', 9, 1, 'green'))
