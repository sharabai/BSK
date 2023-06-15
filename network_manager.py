import socket
from constants import HOST, PORT, BUFFER_SIZE

class NetworkManager:
    def __init__(self, host=HOST, port=PORT, buffer_size=BUFFER_SIZE):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def disconnect(self):
        self.socket.close()

    def send_data(self, data):
        self.socket.sendall(data)

    def receive_data(self):
        return self.socket.recv(self.buffer_size)
