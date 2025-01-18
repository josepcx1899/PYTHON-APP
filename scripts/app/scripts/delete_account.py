import requests

def delete_account(email_entry, password_entry, confirm_password_entry):
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    confirm_password = confirm_password_entry.get().strip()


    if password != confirm_password:
        return 10001

    data = {
        "Email": email,
        "Password": password,
        "ConfirmPassword": confirm_password
    }

    response = requests.delete("http://localhost:5050/delete-account", data=data)

    
    return response.status_code