from customtkinter import *
from scripts.app.scripts.crypto import setup_crypto_list
from scripts.app.scripts.utils import *
from scripts.app.scripts.calculator_and_notepad import open_calculator_and_notepad
from scripts.app.scripts.delete_account import delete_account
from tkinter import messagebox
import time

def launch_dashboard():
    app = CTk()
    app.geometry("1000x700")

    app.iconbitmap("./images/logotipo.ico")

    app.title(" ")

    tabview = CTkTabview(master=app)
    tabview.pack(fill="both", expand=True, padx=20, pady=0)

    tabview.add("Crypto Tool")
    tabview.add("Calculator")
    tabview.add("Delete Account")

    setup_crypto_list(tabview)

    label_2 = CTkLabel(master=tabview.tab("Calculator"), text="This is the Calculator tab")
    label_2.pack(padx=20, pady=20)

    button_calculadora = CTkButton(master=tabview.tab("Calculator"), text="Open Calculator", command=open_calculator_and_notepad)
    button_calculadora.pack(pady=20)

    label_3 = CTkLabel(master=tabview.tab("Delete Account"), text="Delete Account tab")
    label_3.pack(padx=20, pady=20)

    email_entry = CTkEntry(master=tabview.tab("Delete Account"), placeholder_text="Email")
    email_entry.pack(padx=20, pady=10)

    password_entry = CTkEntry(master=tabview.tab("Delete Account"), placeholder_text="Password", show="*")
    password_entry.pack(padx=20, pady=10)

    confirm_password_entry = CTkEntry(master=tabview.tab("Delete Account"), placeholder_text="Confirm Password", show="*")
    confirm_password_entry.pack(padx=20, pady=10)

    def handle_delete_account():
        status_code = delete_account(email_entry, password_entry, confirm_password_entry)
        
        print(status_code)

        if status_code == 200:
            messagebox.showinfo("Success", "Account deleted successfully.\nThe program will close in 5 seconds.", icon="info")
            time.sleep(5)
            app,quit()
        else:
            messagebox.showinfo("Error", "Status code " + status_code, icon="error")



    delete_button = CTkButton(master=tabview.tab("Delete Account"), text="Delete Account", command=handle_delete_account)
    delete_button.pack(pady=20)

    app.mainloop()
