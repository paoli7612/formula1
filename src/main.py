from player import Player
from match import Match
from map import Map
from server import Server

def main():
    map = Map("map1")
    p1 = Player("nome1", 3, 1, "red", map)
    p2 = Player("nome2", 6, 1, "blue", map)
    p3 = Player("nome3", 9, 1, "green", map)
    m = Match(map, p1, p2, p3)
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
    #server()
    #client()
    main()
