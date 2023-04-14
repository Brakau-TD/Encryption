"""this class implements the transposition cipher encryption and decryption"""

from encryption import Encryption


class TranspositionCipher(Encryption):
    def __init__(self):
        self._clear_text = None
        self._encrypted_text = ""
        self._decrypted_text = ""
        self._encrypt_array = []
        self._cipher = 0
        self._rows = None
        pass

    def encrypt(self):
        # create a list of lists to hold the clear text
        self._rows, new_text = self.prepare_algorithm(self._clear_text)
        for row in range(self._rows):
            temp_array = []
            for i in range(len(new_text) // self._rows):
                temp_array.append(new_text[i + (row * self._cipher)])
            self._encrypt_array.append(temp_array)
        # create a string from a rotated array
        for column in range(self._cipher):
            for row in self._encrypt_array:
                self._encrypted_text += row[column]

    def calculate_row_numbers(self, text):
        """returns the number of rows needed to encrypt the text"""
        return (len(text) + self._cipher - 1) // self._cipher

    def transform_text(self, rows, text):
        """adds blanks to the string so that it fits the encryption array"""
        amount_blanks = (rows * self._cipher) - len(text)
        return text + (" " * amount_blanks)

    def decrypt(self):
        self._rows, new_text = self.prepare_algorithm(self._encrypted_text)

    def prepare_algorithm(self, text):
        rows = self.calculate_row_numbers(text)
        new_text = self.transform_text(rows, text)
        return rows, new_text

    def set_clear_text(self, clear_text: str):
        self._clear_text = clear_text

    def set_encrypted_text(self, text):
        self._encrypted_text = text

    def set_cipher(self, cipher: any):
        self._cipher = cipher

    def give_encrypted_text(self) -> str:
        return self._encrypted_text

    def give_decrypted_text(self) -> str:
        return self._decrypted_text


def transposition_testanwendung():
    tc = TranspositionCipher()
    tc.set_clear_text("Hallo von Torsten. Wie geht es dir?")
    tc.set_cipher(4)
    tc.encrypt()
    print(tc.give_encrypted_text())


if __name__ == "__main__":
    transposition_testanwendung()
