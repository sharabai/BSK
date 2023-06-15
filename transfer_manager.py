from constants import BUFFER_SIZE

class TransferManager:
    def __init__(self, network_manager, encryption_manager):
        self.network_manager = network_manager
        self.encryption_manager = encryption_manager

    def send_message(self, message):
        encrypted_message = self.encryption_manager.encrypt_text(message)
        self.network_manager.send_data(encrypted_message)

    def receive_message(self):
        encrypted_message = self.network_manager.receive_data()
        message = self.encryption_manager.decrypt_text(encrypted_message)
        return message

    def send_file(self, file_path):
        with open(file_path, 'rb') as file:
            while (chunk := file.read(BUFFER_SIZE)):
                encrypted_chunk = self.encryption_manager.encrypt_data(chunk)
                self.network_manager.send_data(encrypted_chunk)

    def receive_file(self, file_path):
        with open(file_path, 'wb') as file:
            while (encrypted_chunk := self.network_manager.receive_data()):
                chunk = self.encryption_manager.decrypt_data(encrypted_chunk)
                file.write(chunk)
