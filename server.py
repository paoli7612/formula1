import socket

class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_adress = ("localhost", 10000)
        self.sock.bind(server_adress)
        self.sock.listen(1)
        print("Attesa connessione client")
        self.connection, client_address = self.sock.accept()
        print("Client correttamente connesso", client_address)

        try:
            while True:
            	data = connection.recv(32)
            	message = data.decode()
            	time.sleep(1)
            	if message != "": print(message)
        except:
            print("connection lost")

s = Server()
