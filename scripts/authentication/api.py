import requests

url = "http://localhost:5050/"

def login_api(email, password):
    data = {
        "Email": email,
        "Password": password
    }
    try:
        response = requests.post(url + "login", data=data)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def register_api(email, password, confirm_password):
    data = {
        "Email": email,
        "Password": password,
        "ConfirmPassword": confirm_password
    }
    try:
        response = requests.post(url + "register", data=data)
        return response.json() if response.status_code == 200 else response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def forgotpw(email):
    data = {"Email": email}
    try:
        response = requests.post(url + "forgot-password", data=data)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def submit_code_api(email, code, new_password):
    data = {
        "Email": email,
        "Code": code,
        "NewPassword": new_password
    }
    try:
        response = requests.post(url + "reset-password", data=data)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None