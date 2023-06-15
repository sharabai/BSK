import socket
import threading
from constants import HOST, PORT, BUFFER_SIZE

class NetworkManager:
    def __init__(self, host=HOST, port=PORT, buffer_size=BUFFER_SIZE):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.client_socket = None
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.server_thread = threading.Thread(target=self.accept_connection)
        self.server_thread.start()

    def accept_connection(self):
        while True:
            conn, addr = self.server_socket.accept()
            if self.client_socket is None:
                print(f"Connection accepted from {addr}")
            else:
                conn.close()

    def connect(self):
        if self.client_socket is None:
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((self.host, self.port))
            except ConnectionRefusedError:
                print("Connection failed. Retrying in 5 seconds...")

    def disconnect(self):
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None

    def send_data(self, data):
        if self.client_socket:
            self.client_socket.sendall(data)

    def receive_data(self):
        if self.server_socket:
            return self.server_socket.recv(self.buffer_size)