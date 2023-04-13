"""implements an abstract class for encryption and decryption as a template for other encryption methods"""
from abc import ABC, abstractmethod


class Encryption(ABC):
    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass

    @abstractmethod
    def set_clear_text(self, clear_text: str):
        pass

    @abstractmethod
    def set_decrypted_text(self, decrypted_text: str):
        pass

    @abstractmethod
    def set_cipher(self, cipher: any):
        pass

    @abstractmethod
    def give_encrypted_text(self) -> str:
        pass

    @abstractmethod
    def give_decrypted_text(self) -> str:
        pass
