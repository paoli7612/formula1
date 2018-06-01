from player import Player
from window import Window

def main():
    w = Window()
    p1 = Player("Mario", 5, 7)
    p2 = Player("Giovanni", 9, 7)

    w.draw()
    p1.draw(w.screen)
    w.flip()
    print(p1)
    print(p2)

    import time
    time.sleep(2)


if __name__ == "__main__":
    main()
