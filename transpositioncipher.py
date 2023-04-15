"""this class implements the transposition cipher encryption and decryption"""

from encryption import Encryption


class TranspositionCipher(Encryption):
    def __init__(self):
        self._clear_text = ""
        self._encrypted_text = ""
        self._decrypted_text = ""
        self._encrypt_array = []
        self._cipher = 0

    def encrypt(self):
        """creates an encrypted string in self._encrypted_text from self._clear_text input"""
        # gets the exact number of rows of the array and a transformed text which fits in an array of n-rows with n-columns
        rows, clear_text = self.prepare_algorithm(self._clear_text)
        # writes the clear text (clear_text) into an array of the specified size
        self._encrypt_array = [
            [
                clear_text[i + (row * self._cipher)]
                for i in range(len(clear_text) // rows)
            ]
            for row in range(rows)
        ]
        # "rotate" the self._encrypt_array into its encrypted form
        encrypt_array = [
            [row[column] for row in self._encrypt_array]
            for column in range(self._cipher)
        ]
        flatlist = [item for sublist in encrypt_array for item in sublist]
        self._encrypted_text = "".join(flatlist)

    def calculate_row_numbers(self, text: str) -> int:
        """returns the number of rows needed to encrypt the text"""
        return (len(text) + self._cipher - 1) // self._cipher

    def transform_text(self, rows: int, text: str) -> str:
        """adds blanks to the string so that it fits the encryption array"""
        amount_blanks = (rows * self._cipher) - len(text)
        return text + (" " * amount_blanks)

    def decrypt(self):
        """reverses the encryption proces"""
        rows = self.calculate_row_numbers(self._encrypted_text)
        length, index, counter = len(self._encrypted_text), 0, 0
        while len(self._decrypted_text) < len(self._encrypted_text):
            self._decrypted_text += self._encrypted_text[index]
            index = index + rows
            if index >= length:
                counter += 1
                index = counter

    def prepare_algorithm(self, text: str) -> tuple:
        """logic for creating the two-dimensional array"""
        rows = self.calculate_row_numbers(text)
        new_text = self.transform_text(rows, text)
        return rows, new_text

    def set_clear_text(self, clear_text: str):
        self._clear_text = clear_text

    def set_encrypted_text(self, text: str):
        self._encrypted_text = text

    def set_cipher(self, cipher: int):
        self._cipher = cipher

    def give_encrypted_text(self) -> str:
        return self._encrypted_text

    def give_decrypted_text(self) -> str:
        return self._decrypted_text

    def clear_memory(self):
        """clears out memory between sessions"""
        self.__init__()

    def get_overview(self):
        print("cipher:          ", self._cipher)
        print("clear text:      ", self._clear_text)
        print("encrypted text:  ", self._encrypted_text)
        print("decrypted text:  ", self._decrypted_text)


def transposition_testfunction():
    tc = TranspositionCipher()
    tc.set_clear_text("Welcome to the world of cryptography!")
    tc.set_cipher(4)
    tc.encrypt()
    tc.set_encrypted_text(tc.give_encrypted_text())
    tc.decrypt()
    tc.get_overview()


if __name__ == "__main__":
    transposition_testfunction()
