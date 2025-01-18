import re
from scripts.authentication.api import login_api, register_api, forgotpw, submit_code_api
from scripts.app.main import launch_dashboard
from scripts.authentication.utils import show_login, show_reset_password, open_options_window

def click_handler(label_Email, label_Password, error_label, main_window):
    email = label_Email.get().strip()
    password = label_Password.get().strip()
    error_label.configure(text="")

    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not re.match(email_regex, email):
        error_label.configure(text="Invalid email format.")
    elif len(password) < 6:
        error_label.configure(text="Password must be at least 6 characters long.")
    else:
        code = login_api(email, password)
        if code == 401:
            error_label.configure(text="Invalid email or password")
        elif code == 200:
            main_window.destroy()
            launch_dashboard()
        elif code == 400:
            error_label.configure(text="Email and password are required")
        else:
            error_label.configure(text=f"ERROR!\nStatus code: {code}")

def forgot_password_handler(forgot_email_entry, error_label_forgot, forgot_password_frame, reset_password_frame):
    email = forgot_email_entry.get().strip()
    error_label_forgot.configure(text="")

    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not re.match(email_regex, email):
        error_label_forgot.configure(text="Invalid email format.", text_color="red")
    else:
        r = forgotpw(email)
        if r == 200:
            error_label_forgot.configure(text="If the email exists, a code will be sent.", text_color="green")
            show_reset_password(forgot_password_frame, reset_password_frame)
        else:
            error_label_forgot.configure(text=f"ERROR!", text_color="red")

def submit_code_handler(forgot_email_entry, code_entry, new_password_entry, confirm_new_password_entry, error_label_reset):
    email = forgot_email_entry.get().strip()
    code = code_entry.get().strip()
    new_password = new_password_entry.get().strip()
    confirm_password = confirm_new_password_entry.get().strip()

    if not new_password or len(new_password) < 6:
        error_label_reset.configure(text="Password must be at least 6 characters long.", text_color="red")
    elif new_password != confirm_password:
        error_label_reset.configure(text="Passwords do not match.", text_color="red")
    else:
        code = submit_code_api(email, code, new_password)
        if code == 200:
            error_label_reset.configure(text="Password successfully reset.", text_color="green")
        else:
            error_label_reset.configure(text=f"ERROR!\nStatus code: {code}", text_color="red")

def register_handler(label_Email_Register, label_Password_Register, confirm_password_entry, error_label_register, main_window):
    email = label_Email_Register.get().strip()
    password = label_Password_Register.get().strip()
    confirm_password = confirm_password_entry.get().strip()

    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not re.match(email_regex, email):
        error_label_register.configure(text="Invalid email format.")
    else:
        txt = register_api(email, password, confirm_password)
        if "error" in txt:
            error_label_register.configure(text=txt["error"])
        elif "success" in txt:
            main_window.destroy()
            launch_dashboard()
        else:
            error_label_register.configure(text=f"ERROR!\nStatus Code: {txt}")
