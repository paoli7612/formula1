from player import Player
from match import Match
from map import Map

def main():
    map = Map("map1")
    p1 = Player("nome1", 3, 1, "red", map)
    p2 = Player("nome2", 6, 1, "blue", map)
    p3 = Player("nome3", 9, 1, "green", map)
    m = Match(map, p1, p2, p3)
    m.start()

if __name__ == "__main__":
    main()
