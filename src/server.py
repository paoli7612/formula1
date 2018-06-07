import socket
import struct
import time
import pygame

import conf
from match import Match

class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_adress = ("localhost", conf.PORT)
        self.sock.bind(server_adress)
        self.sock.listen(1)
        print("Attesa connessione client")
        self.connection, client_address = self.sock.accept()
        print("Client correttamente connesso", client_address)

    def send_screen(self, screen):
        image = screen.copy()
        img_str = pygame.image.tostring(image, "RGB")
        len_str = struct.pack("!i", len(img_str))
        self.connection.send(len_str)
        self.connection.send(img_str)

    def send_start(self):
        self.connection.send("start")

    def send_end(self):
        self.connection.send("end")

    def get_event(self):
        pass
