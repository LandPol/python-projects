import os
import tkinter as tk
from tkinter import font
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

def get_weather(city_name):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError:
        print(f"ERROR: City '{city_name}' not found.")
        return None
    except requests.exceptions.RequestException:
        print("ERROR: No internet connection.")
        return None


weather_label = None

def display_weather(data):
    global weather_label
    if weather_label:
        weather_label.destroy()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    weather_label = tk.Label(
        window,
        text=f"Temperature: {temp} C\nWeather: {description}\nHumidity: {humidity}",
        font=("Arial", 15)
        )
    weather_label.config(background="white")
    weather_label.pack(pady=20)

def search():
    city_name = city.get("1.0", "end-1c").strip()
    if city_name and city_name != placeholder:
        data = get_weather(city_name)
        if data:
            display_weather(data)
        else:
            print("No data to display.")

def on_focus_in(event):
    if city.get("1.0", "end-1c") == placeholder:
        city.delete("1.0", "end")
        city.config(fg="black")

def on_focus_out(event):
    if city.get("1.0", "end-1c").strip() == "":
        city.insert("1.0", placeholder)
        city.config(fg="grey")

window = tk.Tk()
window.geometry("420x420")
window.title("Weather App")
window.config(background="lightgreen")

placeholder = "Input a name of the city you want to check: "

city = tk.Text(
    window,
    height=3,
    selectbackground="lightgreen",
    font=("Arial", 15)
    )
city.insert("1.0", placeholder)
city.bind("<FocusIn>", on_focus_in)
city.bind("<FocusOut>", on_focus_out)
city.bind("<Return>", lambda event: search())
city.pack(padx=10, pady=10)

bold_font = font.Font(
    family="Helvetica",
    size=12,
    weight="bold"
    )

btn = tk.Button(
    window,
    text="Search",
    font=bold_font
    )
btn.config(
    background="green",
    foreground="white",
    width=20,
    command=search
    )
btn.pack()


window.mainloop()