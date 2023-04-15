"""Is and inbetween interface between GUI and the encryption methods"""

from caesar import Caesar
from transpositioncipher import TranspositionCipher
from vigenere import Vigenere


class EncryptionDict:
    """holds information about the encryption methods"""

    def __init__(self):
        self.encryption_dict = {1: Caesar, 2: TranspositionCipher, 3: Vigenere}

    def get_encryption_method(self, method):
        # returns an instance of the class
        return self.encryption_dict[method]()


class LogicInterface:
    """
    handles back and forth between GUI and encryption methods
    """

    def __init__(self):
        self._encryption_dict = EncryptionDict()
        self._encrypted_text = None
        self._decrypted_text = None
        self._cipher = None

    def encrypt(self, cleartext, cipher, method):
        result = self.check_input(cleartext, cipher, method)
        if not result:
            return
        self._algorithm = self.get_encryption_method(method)
        self._algorithm.set_clear_text(cleartext)
        self._algorithm.set_cipher(self._cipher)
        self._algorithm.encrypt()
        self._encrypted_text = self._algorithm.give_encrypted_text()

    def decrypt(self, encryptedtext, cipher, method):
        result = self.check_input(encryptedtext, cipher, method)
        if not result:
            return
        self._algorithm = self.get_encryption_method(method)
        self._algorithm.set_encrypted_text(encryptedtext)
        self._algorithm.set_cipher(self._cipher)
        self._algorithm.decrypt()
        self._decrypted_text = self._algorithm.give_decrypted_text()

    def get_encryption_method(self, method):
        return self._encryption_dict.get_encryption_method(method)

    def get_encrypted_text(self):
        return self._encrypted_text

    def get_decrypted_text(self):
        return self._decrypted_text

    def check_input(self, text, cipher, method):
        """checks if the input is valid"""
        if not text:
            return "Please enter a text"
        if not cipher:
            return "Please enter a cipher"
        if method == 0:
            return "Please select a method"
        if method in [1, 2] and not cipher.isdigit():
            return "Please enter a number for the cipher"
        elif method in [1, 2] and cipher.isdigit():
            self._cipher = int(cipher)
            if self._cipher < 1:
                return "Please enter a number greater than 0"
        elif method == 3:
            self._cipher = str(cipher)
        return True

    def clear_memory(self):
        self._encrypted_text = None
        self._decrypted_text = None
        self._cipher = None
        self._algorithm.clear_memory()
