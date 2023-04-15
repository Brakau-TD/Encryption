# Encryption
This repo implements three encryption/decryption methods for educational purposes. Built around an abstract class, the child-classes are meant to give an insight into three classic algorithms.
By no means should these be used for actual encryption of important information, as they are are not secure.
Each class has its own testfunction to test the encryption and decryption methods. This can be accessed by running the files with the encryption algorithms directly as "main".

# On the environment
App is written in and tested on Python 3.10.11. It should work on any Python 3 version, but I can't guarantee it.
The only dependencies are the Tkinter library, which is included in the standard library and
the abc module, which is also included in the standard library.

# Usage
Start the app by running encrypt_a_text.py.

1. Click on a radio button to choose an encryption / decryption algorithm.
2. Enter a text in either the encryption or decryption field.
3. Enter the cipher for the encryption / decryption. Keep in mind:
    - The cipher for the Caesar cipher is an integer.
    - The cipher for the Transposition is an integer.
    - The cipher for the Vigenere cipher is a word.
4. Click on the button to encrypt / decrypt the text.
5. The result will be displayed in the field to the right.
6. Copy the result to your clipboard.
7. You're done!

# Possible improvements
GUI:
- Add a button to clear the text fields manually
- Add a button to copy the cipher to the clipboard
- Add a button to copy the result to the clipboard
- Swap the radio buttons for a dropdown field
Algorithms:
- Add a new algorithm, e.g. the RSA algorithm
- optimize the algorithms

Have fun forking them and adding new algorithms.

Be kind and mindful
