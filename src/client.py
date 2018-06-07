import socket
import pygame
import struct

import conf

class Client:
    def __init__(self):
        self.screen = pygame.display.set_mode(conf.SIZE)
        pygame.display.set_caption(conf.TITLE)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_adress = ("localhost", conf.PORT)
        self.sock.connect(server_adress)

    def run(self):
        image = self.get_screen()
        self.screen.blit(image,(0,0))
        pygame.display.flip()
        

    def get_screen(self):
        len_str = s.recv(4)
        size = struct.unpack('!i', len_str)[0]
        while size > 0:
            if size >= 4096: data = s.recv(4096)
            else: data = s.recv(size)
            if not data: break
            size -= len(data)
            img_str += data
        image = pygame.image.fromstring(img_str, SURFACE_SIZE, 'RGB')
        image_rect = image.get_rect(center=self.screen_rect.center)

c = Client()
