from customtkinter import *
import math
import os
from cryptography.fernet import Fernet
import os


def open_calculator_and_notepad():
    app = CTk()
    app.geometry("1000x700")
    app.minsize(800, 700)
    app.iconbitmap("./images/logotipo.ico")
    app.title(" ")

    entry_style = {
        "width": 300,
        "height": 40,
        "text_color": "black",
        "corner_radius": 40,
        "font": ("Arial", 16, "bold"),
        "fg_color": "#fff"
    }

    main_container = CTkFrame(master=app, fg_color="#323232")
    main_container.pack(fill="both", expand=True, padx=20, pady=20)

    calc_container = CTkFrame(master=main_container, fg_color="#424242", corner_radius=10)
    calc_container.pack(side="left", padx=10, pady=10)

    calc_inner_container = CTkFrame(master=calc_container, fg_color="#424242", corner_radius=10)
    calc_inner_container.pack(expand=True)

    notes_container = CTkFrame(master=main_container, fg_color="#424242", corner_radius=10)
    notes_container.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def obfuscate_key(key: bytes, shift: int = 3) -> str:
        key_str = key.decode()
        obfuscated = ''.join(chr((ord(c) + shift) % 256) for c in key_str)
        return obfuscated

    def deobfuscate_key(obfuscated_key: str, shift: int = 3) -> bytes:
        deobfuscated = ''.join(chr((ord(c) - shift) % 256) for c in obfuscated_key)
        return deobfuscated.encode()

    def get_fernet_key():
        key_directory = os.path.join(os.getenv("APPDATA"), "bullrcs")
        key_path = os.path.join(key_directory, "bullrcs.key")

        if not os.path.exists(key_directory):
            os.makedirs(key_directory)

        if not os.path.exists(key_path):
            fernet_key = Fernet.generate_key()
            obfuscated_key = obfuscate_key(fernet_key)
            with open(key_path, "w") as key_file:
                key_file.write(obfuscated_key)
        else:
            with open(key_path, "r") as key_file:
                obfuscated_key = key_file.read()
                fernet_key = deobfuscate_key(obfuscated_key)

        return fernet_key

    def handle_button_click(button_text):
        if button_text == "C":
            calc_input.delete(0, END)
        elif button_text == "=":
            try:
                result = eval(calc_input.get())
                calc_input.delete(0, END)
                calc_input.insert(0, str(result))
            except Exception as e:
                calc_input.delete(0, END)
                calc_input.insert(0, "Error")
        elif button_text == "√":
            try:
                result = math.sqrt(float(calc_input.get()))
                calc_input.delete(0, END)
                calc_input.insert(0, str(result))
            except Exception as e:
                calc_input.delete(0, END)
                calc_input.insert(0, "Error")
        else:
            calc_input.insert(END, button_text)

    calc_input = CTkEntry(calc_inner_container, width=250, height=50, font=("Arial", 18), corner_radius=10)
    calc_input.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
        ["(", ")", "√", "^"]
    ]

    for i, row in enumerate(buttons):
        for j, btn_text in enumerate(row):
            button = CTkButton(
                calc_inner_container, text=btn_text, width=50, height=50, command=lambda b=btn_text: handle_button_click(b)
            )
            button.grid(row=i + 1, column=j, padx=5, pady=5)

    def encrypt_data(data):
        key = get_fernet_key()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(data):
        key = get_fernet_key()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(data).decode()
        return decrypted_data

    def save_notes_to_file():
        if not os.path.exists("./data"):
            os.makedirs("./data")
        
        encrypted_content = encrypt_data(notes_input.get("1.0", END))
        with open(os.path.join("./data", "notes.txt"), "wb") as file:
            file.write(encrypted_content)

    def load_notes_from_file():
        notes_path = os.path.join("./data", "notes.txt")
        
        if not os.path.exists("./data"):
            os.makedirs("./data")
        
        if not os.path.exists(notes_path):
            with open(notes_path, "wb") as file:
                file.write(encrypt_data(""))
        
        with open(notes_path, "rb") as file:
            encrypted_content = file.read()
        
        decrypted_content = decrypt_data(encrypted_content)
        notes_input.delete("1.0", END)
        notes_input.insert("1.0", decrypted_content)

    notes_input = CTkTextbox(notes_container, width=400, height=500, font=("Arial", 14), corner_radius=10)
    notes_input.pack(fill="both", expand=True, padx=10, pady=10)

    save_notes_button = CTkButton(
        notes_container, text="Save", command=save_notes_to_file, width=120, height=40, corner_radius=10
    )
    save_notes_button.pack(pady=10)

    load_notes_button = CTkButton(
        notes_container, text="Load", command=load_notes_from_file, width=120, height=40, corner_radius=10
    )
    load_notes_button.pack(pady=10)

    app.mainloop()