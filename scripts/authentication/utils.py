from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, TOP, LEFT, X, CENTER

def show_register(register_frame, login_frame):
    login_frame.pack_forget()
    register_frame.pack(fill="both", expand=True)

def show_login(forgot_password_frame, register_frame, reset_password_frame, login_frame):
    forgot_password_frame.pack_forget()
    register_frame.pack_forget()
    reset_password_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def show_forgot_password(login_frame, forgot_password_frame):
    login_frame.pack_forget()
    forgot_password_frame.pack(fill="both", expand=True)

def show_reset_password(forgot_password_frame, reset_password_frame):
    forgot_password_frame.pack_forget()
    reset_password_frame.pack(fill="both", expand=True)

def open_options_window():
    options_window = CTk()
    options_window.geometry("900x750")
    options_window.minsize(900, 750)
    options_window.title("Options")

    def show_frame(frame):
        frame.tkraise()

    calculator_frame = CTkFrame(master=options_window, fg_color="#323232")
    crypto_frame = CTkFrame(master=options_window, fg_color="#323232")
    delete_account_frame = CTkFrame(master=options_window, fg_color="#323232")

    for frame in (calculator_frame, crypto_frame, delete_account_frame):
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)

    CTkLabel(master=calculator_frame, text="Calculator", font=("Arial", 24)).pack(pady=20)
    CTkLabel(master=crypto_frame, text="Crypto Tool", font=("Arial", 24)).pack(pady=20)
    CTkLabel(master=delete_account_frame, text="Delete Account", font=("Arial", 24)).pack(pady=20)

    nav_frame = CTkFrame(master=options_window, fg_color="#424242")
    nav_frame.pack(side=TOP, fill=X)

    calculator_button = CTkButton(master=nav_frame, text="Calculator", command=lambda: show_frame(calculator_frame))
    calculator_button.pack(side=LEFT, padx=10, pady=10)

    crypto_button = CTkButton(master=nav_frame, text="Crypto Tool", command=lambda: show_frame(crypto_frame))
    crypto_button.pack(side=LEFT, padx=10, pady=10)

    delete_account_button = CTkButton(master=nav_frame, text="Delete Account", command=lambda: show_frame(delete_account_frame))
    delete_account_button.pack(side=LEFT, padx=10, pady=10)

    show_frame(calculator_frame)
    options_window.mainloop()