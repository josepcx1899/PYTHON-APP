from customtkinter import *
from scripts.authentication.ui import setup_ui

app = CTk()
app.geometry("900x750")
app.minsize(900, 750)
app.title(" ")
app.iconbitmap("./images/logotipo.ico")

setup_ui(app)

app.mainloop()