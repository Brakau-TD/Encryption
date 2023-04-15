"""a simple TKinter GUI for the Encryption Project"""

from tkinter import *
from logicinterface import LogicInterface


class EncryptGui:
    """
    class for creating smaller popup windows
    """

    def __init__(self):
        self._li = LogicInterface()
        self.create_window("Encryption", 600, 450)
        pass

    def create_window(self, title: str, width: int, height: int):
        self._app = Tk()
        self._app.title(title)
        self._app.geometry(f"{width}x{height}")
        self._clear_text = StringVar()
        self._cipher = StringVar()
        self._encrypted_text = StringVar()
        self._method = IntVar()
        self._frames = self.create_frames()
        self._gui_elements = self.gui_elements()
        self.create_gui_elements()
        self._app.mainloop()

    def create_frames(self) -> dict:
        self._left_frame = Frame(self._app)
        self._left_frame.pack(side=LEFT)
        self._right_frame = Frame(self._app)
        self._right_frame.pack(side=RIGHT)

    def gui_elements(self) -> dict:
        gui_elements = {
            "Choose encryption method": Label(
                self._left_frame, text="Choose encryption method:"
            ),
            "Caesar": Radiobutton(
                self._left_frame, text="Caesar", variable=self._method, value=1
            ),
            "Transposition": Radiobutton(
                self._left_frame, text="Transposition", variable=self._method, value=2
            ),
            "Vigenere": Radiobutton(
                self._left_frame, text="Vigenere", variable=self._method, value=3
            ),
            "Info": Label(self._left_frame, text="Enter text to encrypt:"),
            "Enter your message": Label(self._left_frame, text="Enter your message:"),
            "Clear text": Entry(self._left_frame, textvariable=self._clear_text),
            "Cipher": Label(self._left_frame, text="Enter cipher:"),
            "Cipher entry": Entry(self._left_frame, textvariable=self._cipher),
            "Encrypt": Button(self._left_frame, text="Encrypt", command=self.encrypt),
            "Encrypted text": Label(self._left_frame, text=""),
            "Text for decryption": Label(
                self._left_frame, text="Enter text to decrypt:"
            ),
            "Decrypt entry": Entry(self._left_frame, textvariable=self._encrypted_text),
            "Decrypt": Button(self._left_frame, text="Decrypt", command=self.decrypt),
            "Info": Label(self._right_frame, text="Info:"),
            "Info text": Label(
                self._right_frame,
                text="This is a simple encryption program. \nYou can choose between three different encryption methods: \nCaesar, Vigenere and Transposition. \nYou can also choose between encryption and decryption.",
            ),
            "Output": Text(self._right_frame, width=40, height=15, pady=5, padx=10),
        }
        return gui_elements

    def create_gui_elements(self):
        for key in self._gui_elements:
            self._gui_elements[key].pack(pady=5, padx=5)
        self._gui_elements["Output"].insert(END, "Output: ")

    def encrypt(self):
        self._li.encrypt(self._clear_text.get(), self._cipher.get(), self._method.get())
        self._gui_elements["Output"].delete(0.0, END)
        self._gui_elements["Output"].insert(0.0, self._li.get_encrypted_text())
        self._clear_gui()

    def decrypt(self):
        self._li.decrypt(
            self._encrypted_text.get(), self._cipher.get(), self._method.get()
        )
        self._gui_elements["Output"].delete(0.0, END)
        self._gui_elements["Output"].insert(0.0, self._li.get_decrypted_text())
        self._clear_gui()

    def error_message(self, result: str):
        if result is not True:
            self._gui_elements["Output"].delete(0, END)
            self._gui_elements["Output"].insert(0, result)
            return False
        return True

    def _clear_gui(self):
        self._gui_elements["Clear text"].delete(0, END)
        self._gui_elements["Cipher entry"].delete(0, END)
        self._gui_elements["Decrypt entry"].delete(0, END)
        self._li.clear_memory()


def encryptgui():
    gui = EncryptGui()


if __name__ == "__main__":
    encryptgui()
