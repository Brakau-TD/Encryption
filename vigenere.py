"""this class implements the Vigenére cipher encryption and decryption"""

from encryption import Encryption


class Vigenere(Encryption):
    def __init__(self):
        self._vigenere_rect = []
        self._clear_text_column = []
        self._clear_text = ""
        self._decrypted_text = ""
        self._encrypted_text = ""
        self._cipher = ""
        self._real_start = 32
        self._real_highest = 126
        self._create_vigenere_array()

    def _create_vigenere_array(self):
        """creates an array with a given alphabet range constructed from ascii codes, each line being shifted"""
        array, counter = [], -1
        index_difference = self._real_highest - self._real_start
        for _ in range(0, index_difference):
            counter += 1
            array = []
            for i in range(0, index_difference):
                value = self._real_start + i + counter
                if value > self._real_highest:
                    value = self._real_start + (i - (index_difference - 1)) + counter
                array.append(chr(value))
            self._vigenere_rect.append(array)
        self._clear_text_column = [
            chr(x) for x in range(self._real_start, self._real_highest)
        ]

    def _set_cipher_to_cleartext_length(self, textforlength: str = None):
        """both strings need to be the same length"""
        ci, ct = len(self._cipher), len(textforlength)
        if ci > ct:
            self._cipher = self._truncate_cipher(self._cipher, textforlength)
        else:
            self._cipher *= -(-ct // ci)
            self._cipher = self._truncate_cipher(self._cipher, textforlength)

    def _truncate_cipher(self, cipher, cleartext):
        """cipher needs to be as long as cleartext"""
        return cipher[: len(cleartext)]

    def encrypt(self):
        self._set_cipher_to_cleartext_length(self._clear_text)
        for index, letter in enumerate(self._clear_text):
            key_cipher = self._vigenere_rect[0].index(self._cipher[index])
            clear_cipher = self._clear_text_column.index(letter)
            self._encrypted_text += self._vigenere_rect[clear_cipher][key_cipher]

    def decrypt(self):
        """reverses the steps of the encryption"""
        self._set_cipher_to_cleartext_length(self._encrypted_text)
        for index, letter in enumerate(self._encrypted_text):
            key_cipher = self._clear_text_column.index(self._cipher[index])
            decrypted_cipher = self._vigenere_rect[key_cipher].index(letter)
            self._decrypted_text += chr(decrypted_cipher + self._real_start)

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

    def set_start_stop_ascii_code(self, start: int, stop: int):
        """needs to consistent over encryption and decryption"""
        self._real_start = start
        self._real_highest = stop

    def clear_memory(self):
        """clears out memory between sessions"""
        self.__init__()
    
    def get_overview(self):
        print("cipher:          ", self._cipher)
        print("clear text:      ", self._clear_text)
        print("encrypted text:  ", self._encrypted_text)
        print("decrypted text:  ", self._decrypted_text)


def vigenere_testfunction():
    v = Vigenere()
    v.set_start_stop_ascii_code(32, 126)
    v.set_cipher("I am a boring cipher")
    v.set_clear_text("Welcome to the world of cryptography!")
    v.encrypt()
    encrypted = v.give_encrypted_text()
    print("Overview over encryption: ")
    v.get_overview()
    # the delete statement is to "prove" that the memory is cleared
    del v

    vx = Vigenere()
    vx.set_cipher("I am a boring cipher")
    vx.set_encrypted_text(encrypted)
    vx.decrypt()
    print("Overview over decryption: ")
    vx.get_overview()


if __name__ == "__main__":
    vigenere_testfunction()
