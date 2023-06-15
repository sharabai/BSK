from Crypto.Cipher import AES
from key_manager import KeyManager

class EncryptionManager:
    def __init__(self, key_manager):
        self.key_manager = key_manager

    def encrypt_text(self, text):
        aes = self.get_aes_cipher()
        return aes.encrypt(text)

    def decrypt_text(self, encrypted_text):
        aes = self.get_aes_cipher()
        return aes.decrypt(encrypted_text)

    def encrypt_data(self, data):
        aes = self.get_aes_cipher()
        return aes.encrypt(data)

    def decrypt_data(self, encrypted_data):
        aes = self.get_aes_cipher()
        return aes.decrypt(encrypted_data)

    def get_aes_cipher(self):
        aes_key = self.key_manager.get_aes_key()
        aes_iv = self.key_manager.get_aes_iv()
        return AES.new(aes_key, AES.MODE_CBC, iv=aes_iv)
