from network_manager import NetworkManager
from gui_manager import GuiManager
from encryption_manager import EncryptionManager
from key_manager import KeyManager

class ChatApp:
    def __init__(self, host, port):
        self.network_manager = NetworkManager(host, port)
        self.key_manager = KeyManager()
        self.encryption_manager = EncryptionManager(self.key_manager)
        self.gui_manager = GuiManager(self)

        # Connect to the server when the application starts
        self.network_manager.connect()

    def run(self):
        self.gui_manager.run()

    def send_message(self, message):
        encrypted_message = self.encryption_manager.encrypt_text(message)  # Change this line
        self.network_manager.send_data(encrypted_message)

    def receive_data(self, data):
        decrypted_data = self.encryption_manager.decrypt_data(data)  # Change this line
        self.gui_manager.update_chat(decrypted_data)

    def send_file(self, filename):
        with open(filename, 'rb') as file:
            data = file.read()
        encrypted_file = self.encryption_manager.encrypt_data(data)  # Change this line
        self.network_manager.send_data(encrypted_file)

    def receive_file(self, data):
        decrypted_file = self.encryption_manager.decrypt_data(data)  # Change this line
        self.gui_manager.save_file(decrypted_file)
