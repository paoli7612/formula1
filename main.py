from player import Player
from window import Window
from dest import Dest
from event_handler import EventHandler

def main():
    w = Window()
    p = Player("Mario", 5, 7)
    e = EventHandler()
    d = Dest(5, 7)
    w.draw()
    p.draw(w.screen)
    d.draw(w.screen)
    w.flip()
    running = True
    while running:
        v = e.run()
        if v == "quit":
            running = False
        else:
            print("ciao", v)


if __name__ == "__main__":
    main()
