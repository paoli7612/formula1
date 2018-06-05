import socket

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_adress = ("localhost", 10000)
        self.sock.connect(server_adress)

        while True:
        	message = input()
        	data = message.encode()
        	self.sock.sendall(data)

c = Client()
