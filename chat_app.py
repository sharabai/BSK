from network_manager import NetworkManager
from gui_manager import GuiManager
from encryption_manager import EncryptionManager
from key_manager import KeyManager

class ChatApp:
    def __init__(self):
        key_manager = KeyManager()  # Add this line
        self.encryption_manager = EncryptionManager(key_manager)  # Change this line
        self.network_manager = NetworkManager(self)
        self.gui_manager = GuiManager(self)

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
