# main.py
# Frontend (GUI) for the Weather Forecast App
# Modern, card-style design using pure Tkinter (no extra libraries needed)

import tkinter as tk
from tkinter import messagebox
from weather import get_weather

# ---------- Color palette (change these hex codes to re-theme the whole app) ----------
BG_COLOR = "#0f172a"        # dark navy background
CARD_COLOR = "#1e293b"      # slightly lighter navy for the card
ACCENT_COLOR = "#38bdf8"    # sky blue accent (button, highlights)
ACCENT_HOVER = "#0ea5e9"    # darker blue when button is hovered
TEXT_PRIMARY = "#f8fafc"    # near-white text
TEXT_SECONDARY = "#94a3b8"  # muted gray text for labels
ERROR_COLOR = "#f87171"     # soft red for errors

FONT_MAIN = "Segoe UI"      # clean modern font (falls back gracefully if unavailable)


def on_search():
    """Runs when the Get Weather button is clicked."""
    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    # Show a temporary "loading" state so the UI feels responsive
    result_title.config(text="Fetching weather...", fg=TEXT_SECONDARY)
    window.update_idletasks()  # force the UI to repaint immediately

    result = get_weather(city)

    if "error" in result:
        result_title.config(text="⚠ " + result["error"], fg=ERROR_COLOR)
        temp_value.config(text="--°C")
        detail_humidity.config(text="Humidity: -")
        detail_condition.config(text="Condition: -")
        detail_wind.config(text="Wind: -")
        return

    # Success — populate the card with real data
    result_title.config(text=f"{result['city']}", fg=TEXT_PRIMARY)
    temp_value.config(text=f"{result['temperature']}°C")
    detail_humidity.config(text=f"💧 Humidity: {result['humidity']}%")
    detail_condition.config(text=f"☁ Condition: {result['condition']}")
    detail_wind.config(text=f"🌬 Wind: {result['wind_speed']} m/s")


def on_enter_key(event):
    """Allow pressing Enter in the input box to trigger a search."""
    on_search()


def on_button_hover(event):
    search_button.config(bg=ACCENT_HOVER)


def on_button_leave(event):
    search_button.config(bg=ACCENT_COLOR)


# ---------- Main window setup ----------
window = tk.Tk()
window.title("Weather Forecast App")
window.geometry("420x560")
window.config(bg=BG_COLOR)
window.resizable(True, True)  # fixed size looks cleaner for this layout

# ---------- Heading ----------
heading = tk.Label(
    window, text="Weather Forecast",
    font=(FONT_MAIN, 22, "bold"), bg=BG_COLOR, fg=TEXT_PRIMARY
)
heading.pack(pady=(35, 5))

subheading = tk.Label(
    window, text="Check live weather for any city",
    font=(FONT_MAIN, 11), bg=BG_COLOR, fg=TEXT_SECONDARY
)
subheading.pack(pady=(0, 25))

# ---------- Search row (entry + button) ----------
search_frame = tk.Frame(window, bg=BG_COLOR)
search_frame.pack(pady=(0, 30))

city_entry = tk.Entry(
    search_frame, font=(FONT_MAIN, 13), width=18,
    bg=CARD_COLOR, fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY,
    relief="flat", justify="center"
)
city_entry.pack(side="left", ipady=8, padx=(0, 8))
city_entry.bind("<Return>", on_enter_key)  # pressing Enter also searches
city_entry.focus()  # cursor starts in this box automatically

search_button = tk.Button(
    search_frame, text="Search", font=(FONT_MAIN, 11, "bold"),
    bg=ACCENT_COLOR, fg="#0f172a", activebackground=ACCENT_HOVER,
    relief="flat", cursor="hand2", command=on_search, padx=16
)
search_button.pack(side="left", ipady=6)
search_button.bind("<Enter>", on_button_hover)  # mouse hover effect
search_button.bind("<Leave>", on_button_leave)

# ---------- Weather card ----------
card = tk.Frame(window, bg=CARD_COLOR, width=340, height=340)
card.pack(pady=10)
card.pack_propagate(False)  # keeps the card a fixed size regardless of content

result_title = tk.Label(
    card, text="Search a city to begin",
    font=(FONT_MAIN, 15, "bold"), bg=CARD_COLOR, fg=TEXT_SECONDARY,
    wraplength=300
)
result_title.pack(pady=(30, 10))

temp_value = tk.Label(
    card, text="--°C",
    font=(FONT_MAIN, 42, "bold"), bg=CARD_COLOR, fg=ACCENT_COLOR
)
temp_value.pack(pady=(0, 25))

# Divider line for visual separation
divider = tk.Frame(card, bg="#334155", height=1, width=280)
divider.pack(pady=(0, 20))

detail_humidity = tk.Label(
    card, text="💧 Humidity: -",
    font=(FONT_MAIN, 12), bg=CARD_COLOR, fg=TEXT_SECONDARY
)
detail_humidity.pack(pady=6)

detail_condition = tk.Label(
    card, text="☁ Condition: -",
    font=(FONT_MAIN, 12), bg=CARD_COLOR, fg=TEXT_SECONDARY
)
detail_condition.pack(pady=6)

detail_wind = tk.Label(
    card, text="🌬 Wind: -",
    font=(FONT_MAIN, 12), bg=CARD_COLOR, fg=TEXT_SECONDARY
)
detail_wind.pack(pady=6)

# ---------- Footer ----------
footer = tk.Label(
    window, text="Powered by OpenWeatherMap API",
    font=(FONT_MAIN, 9), bg=BG_COLOR, fg="#475569"
)
footer.pack(side="bottom", pady=15)

window.mainloop()
