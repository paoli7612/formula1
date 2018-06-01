from player import Player
from window import Window
from event_handler import EventHandler

def main():
    w = Window()
    p = Player("Mario", 5, 7)
    e = EventHandler()

    w.draw()
    p.draw(w.screen)
    w.flip()
    print(e.run())



if __name__ == "__main__":
    main()
