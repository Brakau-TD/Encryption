"""class for simple encryption and decryption of text using the Caesar cipher."""

class Caesar:
    def __init__(self):
        self._clear_text = None
        self._encrypted_text = None
        self._decrypted_text = ""
        self._encryption_start = 0
    
    def set_clear_text(self, clear_text: str):
        self._clear_text = clear_text
    
    def give_encrypted_text(self) -> str:
        return self._encrypted_text
    
    def give_decrypted_text(self) -> str:
        return self._decrypted_text
    
    def set_encryption_start(self, encryption_start: int):
        self._encryption_start = encryption_start
    
    def encrypt(self):
        self._encrypted_text = ""
        for letter in self._clear_text:
            encrypted_letter = ord(letter) + self._encryption_start
            encrypted_letter = 48 + (encrypted_letter - 122) if encrypted_letter > 125 else encrypted_letter
            self._encrypted_text = self._encrypted_text + chr(encrypted_letter)
    
    def decrypt(self, decryption_key: int):
        """returns the string of the decrypted text"""
        for letter in self._encrypted_text:
            decrypted_letter = ord(letter) - decryption_key
            if decrypted_letter <48:
                decrypted_letter = 122 - abs(decrypted_letter -48)
            self._decrypted_text += chr(decrypted_letter)

caesar = Caesar()
caesar.set_clear_text("0Helloz")
caesar.set_encryption_start(3)
caesar.encrypt()
print(caesar.give_encrypted_text())
caesar.decrypt(3)
print(caesar.give_decrypted_text())