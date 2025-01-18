from customtkinter import *
from PIL import Image
from scripts.authentication.handlers import click_handler, forgot_password_handler, submit_code_handler, register_handler
from scripts.authentication.utils import show_register, show_login, show_forgot_password, show_reset_password

def setup_ui(app):
    entry_style = {
        "width": 300,
        "height": 40,
        "text_color": "black",
        "corner_radius": 40,
        "font": ("Arial", 16, "bold"),
        "fg_color": "#fff"
    }

    main_frame = CTkFrame(master=app, fg_color="#323232")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    user = Image.open("./images/user.png")
    user_resized = user.resize((300, 300))
    user_path = CTkImage(user, size=(300, 300))

    login_frame = CTkFrame(master=main_frame, fg_color="#323232")
    login_frame.pack(fill="both", expand=True)

    label_img_user_login = CTkLabel(master=login_frame, image=user_path, text="")
    label_img_user_login.pack(pady=20)

    label_Email = CTkEntry(master=login_frame, placeholder_text="Email", **entry_style)
    label_Email.pack(pady=10)

    label_Password = CTkEntry(master=login_frame, placeholder_text="Password", **entry_style, show="*")
    label_Password.pack(pady=10)

    error_label = CTkLabel(master=login_frame, text="", text_color="red", font=("Arial", 12, "italic"))
    error_label.pack(pady=5)

    btn_login = CTkButton(master=login_frame, text="Login", corner_radius=40, fg_color="#009d51", command=lambda: click_handler(label_Email, label_Password, error_label, app),
                          width=100, height=40, font=("Arial", 16, "bold"))
    btn_login.pack(pady=20)

    navigation_frame = CTkFrame(master=login_frame, fg_color="transparent")
    navigation_frame.pack(pady=10)

    label_criarConta_login = CTkLabel(master=navigation_frame, text="Are you new here?", font=("Arial", 14))
    label_criarConta_login.pack(side="left", padx=5)

    label_register = CTkLabel(master=navigation_frame, text="Register", text_color="blue", cursor="hand2", font=("Arial", 14))
    label_register.pack(side="left", padx=5)
    label_register.bind("<Button-1>", lambda e: show_register(register_frame, login_frame))

    forgot_password_label = CTkLabel(master=login_frame, text="Forgot Password?", text_color="blue", cursor="hand2", font=("Arial", 14))
    forgot_password_label.pack(pady=10)
    forgot_password_label.bind("<Button-1>", lambda e: show_forgot_password(login_frame, forgot_password_frame))

    register_frame = CTkFrame(master=main_frame, fg_color="#323232")
    register_frame.pack_forget()

    label_img_user_register = CTkLabel(master=register_frame, image=user_path, text="")
    label_img_user_register.pack(pady=20)

    label_Email_Register = CTkEntry(master=register_frame, placeholder_text="Email", **entry_style)
    label_Email_Register.pack(pady=10)

    label_Password_Register = CTkEntry(master=register_frame, placeholder_text="Password", **entry_style, show="*")
    label_Password_Register.pack(pady=10)

    confirm_password_entry = CTkEntry(master=register_frame, placeholder_text="Confirm Password", **entry_style, show="*")
    confirm_password_entry.pack(pady=10)

    error_label_register = CTkLabel(master=register_frame, text="", text_color="red", font=("Arial", 12, "italic"))
    error_label_register.pack(pady=5)

    btn_register = CTkButton(master=register_frame, text="Register", corner_radius=40, fg_color="#0059b3", command=lambda: register_handler(label_Email_Register, label_Password_Register, confirm_password_entry, error_label_register, app),
                             width=100, height=40, font=("Arial", 16, "bold"))
    btn_register.pack(pady=20)

    navigation_frame_register = CTkFrame(master=register_frame, fg_color="transparent")
    navigation_frame_register.pack(pady=10)

    label_criarConta_register = CTkLabel(master=navigation_frame_register, text="Already have an account?", font=("Arial", 14))
    label_criarConta_register.pack(side="left", padx=5)

    label_login_back = CTkLabel(master=navigation_frame_register, text="Back to Login", text_color="blue", cursor="hand2", font=("Arial", 14))
    label_login_back.pack(side="left", padx=5)
    label_login_back.bind("<Button-1>", lambda e: show_login(forgot_password_frame, register_frame, reset_password_frame, login_frame))

    forgot_password_frame = CTkFrame(master=main_frame, fg_color="#323232")
    forgot_password_frame.pack_forget()

    label_img_user_forgot = CTkLabel(master=forgot_password_frame, image=user_path, text="")
    label_img_user_forgot.pack(pady=20)

    forgot_email_entry = CTkEntry(master=forgot_password_frame, placeholder_text="Enter your email", **entry_style)
    forgot_email_entry.pack(pady=20)

    btn_forgot_password = CTkButton(master=forgot_password_frame, text="Submit Email", corner_radius=40, fg_color="#ff6600", command=lambda: forgot_password_handler(forgot_email_entry, error_label_forgot, forgot_password_frame, reset_password_frame),
                                    width=100, height=40, font=("Arial", 16, "bold"))
    btn_forgot_password.pack(pady=20)

    error_label_forgot = CTkLabel(master=forgot_password_frame, text="", text_color="red", font=("Arial", 12, "italic"))
    error_label_forgot.pack(pady=5)

    navigation_frame_forgot = CTkFrame(master=forgot_password_frame, fg_color="transparent")
    navigation_frame_forgot.pack(pady=10)

    label_criarConta_forgot = CTkLabel(master=navigation_frame_forgot, text="Already have an account?", font=("Arial", 14))
    label_criarConta_forgot.pack(side="left", padx=5)

    label_login_back_forgot = CTkLabel(master=navigation_frame_forgot, text="Back to Login", text_color="blue", cursor="hand2", font=("Arial", 14))
    label_login_back_forgot.pack(side="left", padx=5)
    label_login_back_forgot.bind("<Button-1>", lambda e: show_login(forgot_password_frame, register_frame, reset_password_frame, login_frame))

    reset_password_frame = CTkFrame(master=main_frame, fg_color="#323232")
    reset_password_frame.pack_forget()

    label_img_user_reset = CTkLabel(master=reset_password_frame, image=user_path, text="")
    label_img_user_reset.pack(pady=20)

    code_entry = CTkEntry(master=reset_password_frame, placeholder_text="Enter the code", **entry_style)
    code_entry.pack(pady=10)

    new_password_entry = CTkEntry(master=reset_password_frame, placeholder_text="New Password", **entry_style, show="*")
    new_password_entry.pack(pady=10)

    confirm_new_password_entry = CTkEntry(master=reset_password_frame, placeholder_text="Confirm New Password", **entry_style, show="*")
    confirm_new_password_entry.pack(pady=10)

    error_label_reset = CTkLabel(master=reset_password_frame, text="", text_color="red", font=("Arial", 12, "italic"))
    error_label_reset.pack(pady=5)

    btn_reset_password = CTkButton(master=reset_password_frame, text="Reset Password", corner_radius=40, fg_color="#ff6600", command=lambda: submit_code_handler(forgot_email_entry, code_entry, new_password_entry, confirm_new_password_entry, error_label_reset),
                                    width=100, height=40, font=("Arial", 16, "bold"))
    btn_reset_password.pack(pady=20)

    navigation_frame_reset = CTkFrame(master=reset_password_frame, fg_color="transparent")
    navigation_frame_reset.pack(pady=10)

    label_criarConta_reset = CTkLabel(master=navigation_frame_reset, text="Already have an account?", font=("Arial", 14))
    label_criarConta_reset.pack(side="left", padx=5)

    label_login_back_reset = CTkLabel(master=navigation_frame_reset, text="Back to Login", text_color="blue", cursor="hand2", font=("Arial", 14))
    label_login_back_reset.pack(side="left", padx=5)
    label_login_back_reset.bind("<Button-1>", lambda e: show_login(forgot_password_frame, register_frame, reset_password_frame, login_frame))