import pygame

import conf

class Font:
    def __init__(self, size, color):
        self.font_name = pygame.font.match_font(conf.FONT_NAME)
        self.font = pygame.font.Font(self.font_name, size)
        self.color = color

    def write(self, surface, text, x, y):
        text_surface = self.font.render(text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)


if __name__ == "__main__":
    # test
    pygame.mixer.init()
    pygame.init()
    s = pygame.display.set_mode(conf.SIZE)
    f = Font(20, (255,0,100))
    f.write(s, "ciao", 50,15)

    pygame.display.flip()
    import time
    time.sleep(2)
