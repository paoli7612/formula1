from player import Player
from match import Match

def main():
    p1 = Player("nome1", 10, 10, "red")
    p2 = Player("nome2", 10, 12, "blue")
    m = Match(p1)
    m.start()

if __name__ == "__main__":
    main()
