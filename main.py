from player import Player
from match import Match

def main():
    me = Player("lele", 10, 10)
    you = Player("asd", 10, 12)
    he = Player("foo", 10, 14)

    m = Match(me,you,he)
    m.start()


if __name__ == "__main__":
    main()
