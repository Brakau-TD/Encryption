"""class for simple encryption and decryption of text using the Caesar cipher."""
from encryption import Encryption


class Caesar(Encryption):
    def __init__(self):
        self._clear_text = None
        self._encrypted_text = None
        self._decrypted_text = ""
        self._caesar_cipher = 0

    def set_clear_text(self, clear_text: str):
        self._clear_text = clear_text

    def set_encrypted_text(self, encrypted_text: str):
        self._encrypted_text = encrypted_text

    def give_encrypted_text(self) -> str:
        return self._encrypted_text

    def give_decrypted_text(self) -> str:
        return self._decrypted_text

    def set_cipher(self, caesar_cipher: int):
        """Cipher for encryption and decryption is the same."""
        self._caesar_cipher = caesar_cipher

    def encrypt(self):
        """encrypts a string with the Caesar cipher using the caesar_cipher value"""
        self._encrypted_text = ""
        for letter in self._clear_text:
            encrypted_letter = ord(letter) + self._caesar_cipher
            encrypted_letter = (
                32 + (encrypted_letter - 122)
                if encrypted_letter > 125
                else encrypted_letter
            )
            self._encrypted_text = self._encrypted_text + chr(encrypted_letter)

    def decrypt(self):
        """returns the string of the decrypted text using the caesar_cipher value"""
        for letter in self._encrypted_text:
            decrypted_letter = ord(letter) - self._caesar_cipher
            if decrypted_letter < 32:
                decrypted_letter = 122 - abs(decrypted_letter - 48)
            self._decrypted_text += chr(decrypted_letter)

    def clear_memory(self):
        """clears out memopry between session"""
        self.__init__()


def caesar_testanwendung():
    c = Caesar()
    c.set_clear_text("Willkommen in der Welt der Kryptographie")
    c.set_cipher(4)
    c.encrypt()
    print(c.give_encrypted_text())
    c.set_encrypted_text(c.give_encrypted_text())
    c.set_cipher(4)
    c.decrypt()
    print(c.give_decrypted_text())
    c.clear_memory()


if __name__ == "__main__":
    caesar_testanwendung()
