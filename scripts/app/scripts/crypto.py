from customtkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox, Canvas, Scrollbar, Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scripts.app.scripts.utils import *

current_page = 1

def fetch_crypto_data(page=1):
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/coins/markets",
            params={"vs_currency": "eur", "order": "market_cap_desc", "per_page": 20, "page": page},
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
        return []

def show_crypto_chart(crypto_id, tabview):
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart",
            params={"vs_currency": "eur", "days": "7"},
        )
        response.raise_for_status()
        data = response.json()

        prices = [point[1] for point in data["prices"]]
        dates = [i for i in range(len(prices))]

        figure = plt.Figure(figsize=(6, 4), dpi=100)
        ax = figure.add_subplot(111)
        ax.plot(dates, prices, label="Price (EUR)")
        ax.set_title(f"Price Chart: {crypto_id}")
        ax.set_xlabel("Last 7 Days")
        ax.set_ylabel("Price (EUR)")
        ax.legend()

        for widget in tabview.tab("Crypto Tool").winfo_children():
            widget.destroy()
        chart = FigureCanvasTkAgg(figure, tabview.tab("Crypto Tool"))
        chart.get_tk_widget().pack(fill="both", expand=True)

        back_button = CTkButton(
            tabview.tab("Crypto Tool"),
            text="Back",
            command=lambda: restore_crypto_list(tabview)
        )
        back_button.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load chart: {e}")

def restore_crypto_list(tabview):
    for widget in tabview.tab("Crypto Tool").winfo_children():
        widget.destroy()
    setup_crypto_list(tabview)

def setup_crypto_list(tabview):
    outer_frame = Frame(tabview.tab("Crypto Tool"), bg="#2b2b2b")
    outer_frame.pack(fill="both", expand=True, padx=20, pady=20)

    canvas = Canvas(outer_frame, bg="#2b2b2b", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    scrollbar = Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    global crypto_frame
    crypto_frame = Frame(canvas, bg="#2b2b2b")
    canvas.create_window((0, 0), window=crypto_frame, anchor="nw", width=800)

    crypto_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    canvas.bind_all("<Button-4>", on_mouse_wheel)
    canvas.bind_all("<Button-5>", on_mouse_wheel)

    update_crypto_list(tabview)

def update_crypto_list(tabview, page=1):
    global current_page
    current_page = page
    cryptos = fetch_crypto_data(page)
    
    for widget in crypto_frame.winfo_children():
        widget.destroy()

    for crypto in cryptos:
        try:
            response = requests.get(crypto["image"])
            response.raise_for_status()
            image_data = BytesIO(response.content)
            img = Image.open(image_data).resize((40, 40), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            frame = CTkFrame(crypto_frame, fg_color="transparent")
            frame.pack(fill="x", pady=5, padx=10)

            img_label = CTkLabel(frame, image=img_tk, text="")
            img_label.image = img_tk
            img_label.pack(side="left", padx=10, pady=5)

            name_label = CTkLabel(frame, text=f"{crypto['name']}", font=("Arial", 16), anchor="w")
            name_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            price_label = CTkLabel(frame, text=f"€{crypto['current_price']:.2f}", font=("Arial", 16), anchor="e")
            price_label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            chart_button = CTkButton(
                frame,
                text="View Chart",
                command=lambda c_id=crypto["id"]: show_crypto_chart(c_id, tabview),
                width=100,
            )
            chart_button.pack(side="right", padx=10, pady=5)

            separator = Canvas(crypto_frame, height=1, bg="gray", bd=0, highlightthickness=0)
            separator.pack(fill="x", pady=5)
        except Exception as e:
            print(f"Error loading data for {crypto['name']}: {e}")

    add_pagination_buttons(tabview)

def add_pagination_buttons(tabview):
    for widget in tabview.tab("Crypto Tool").winfo_children():
        if isinstance(widget, CTkButton):
            widget.destroy()

    if current_page > 1:
        prev_button = CTkButton(
            tabview.tab("Crypto Tool"),
            text=f"{current_page - 1}",
            command=lambda: update_crypto_list(tabview, current_page - 1),
            width=5,
            corner_radius=30
        )
        prev_button.pack(side="left", padx=10, pady=10)

    next_button = CTkButton(
        tabview.tab("Crypto Tool"),
            text=f"{current_page + 1}",
            command=lambda: update_crypto_list(tabview, current_page + 1),
            width=5,
            corner_radius=30
    )
    next_button.pack(side="right", padx=10, pady=10)