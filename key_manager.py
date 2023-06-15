import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from constants import AES_KEY_SIZE, AES_IV_SIZE, RSA_KEY_SIZE

class KeyManager:
    def __init__(self):
        self.rsa_key = RSA.generate(RSA_KEY_SIZE)
        self.aes_key = get_random_bytes(AES_KEY_SIZE)
        self.aes_iv = get_random_bytes(AES_IV_SIZE)

    def get_rsa_key(self):
        return self.rsa_key

    def get_aes_key(self):
        return self.aes_key

    def get_aes_iv(self):
        return self.aes_iv

    def save_rsa_key(self, file_path):
        with open(file_path, 'wb') as file:
            file.write(self.rsa_key.export_key())

    def load_rsa_key(self, file_path):
        with open(file_path, 'rb') as file:
            self.rsa_key = RSA.import_key(file.read())

    def encrypt_and_save_rsa_key(self, file_path, password):
        aes_cipher = AES.new(password, AES.MODE_CBC)
        encrypted_rsa_key = aes_cipher.encrypt(pad(self.rsa_key.export_key(), AES.block_size))
        with open(file_path, 'wb') as file:
            file.write(aes_cipher.iv)
            file.write(encrypted_rsa_key)

    def load_and_decrypt_rsa_key(self, file_path, password):
        with open(file_path, 'rb') as file:
            aes_iv = file.read(16)
            encrypted_rsa_key = file.read()
        aes_cipher = AES.new(password, AES.MODE_CBC, iv=aes_iv)
        decrypted_rsa_key = unpad(aes_cipher.decrypt(encrypted_rsa_key), AES.block_size)
        self.rsa_key = RSA.import_key(decrypted_rsa_key)
