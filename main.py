from player import Player
from match import Match

def main():
    me = Player("lele", 10, 10, "red")

    m = Match(me)
    m.start()


if __name__ == "__main__":
    main()
