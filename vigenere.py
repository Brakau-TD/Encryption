"""this class implements the Vigenére cipher encryption and decryption"""

from encryption import Encryption


class Vigenere(Encryption):
    def __init__(self):
        self._create_vigenere_array()
        self._vigenere_rect = []
        self._decrypted_text = ""
        self._cipher = ""
        pass

    def _create_vigenere_array(self):
        """creates an array with a given alphabet range constructed from ascii codes, each line being shifted"""
        array, counter = [], -1
        real_start = 32
        real_highest = 126
        index_difference = real_highest - real_start
        for b in range(0, index_difference):
            counter += 1
            array = []
            for i in range(0, index_difference):
                value = (real_start + i + counter)
                if value > real_highest:
                    value = real_start+(i-(index_difference-1))+counter
                array.append(chr(value))
            self._vigenere_rect.append(array)

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def set_clear_text(self, clear_text: str):
        self._clear_text = clear_text

    def set_encrypted_text(self, text):
        self._encrypted_text = text

    def set_cipher(self, cipher: str):
        self._cipher = cipher

    def give_encrypted_text(self) -> str:
        return self._encrypted_text

    def give_decrypted_text(self) -> str:
        return self._decrypted_text

    def clear_memory(self):
        """clears out memory between sessions"""
        self.__init__()


def vigenere_testanwendung():
    v = Vigenere()
    v.set_cipher("whatabeautifulday")
    v.set_clear_text("Willkommen in der Welt der Kryptographie")


if __name__ == "__main__":
    vigenere_testanwendung()
