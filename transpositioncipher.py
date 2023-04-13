"""this class implements the transposition cipher encryption and decryption"""

from encryption import Encryption


class TranspositionCipher(Encryption):
    def __init__(self):
        self._clear_text = None
        self._encrypted_text = None
        self._decrypted_text = ""
        self._caesar_cipher = 0
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def set_clear_text(self, clear_text: str):
        pass

    def set_decrypted_text(self, decrypted_text: str):
        pass

    def set_cipher(self, cipher: any):
        pass

    def give_encrypted_text(self) -> str:
        pass

    def give_decrypted_text(self) -> str:
        pass
