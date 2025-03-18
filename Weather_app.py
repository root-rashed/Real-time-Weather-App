from tkinter import *
from tkinter import messagebox
import requests

# Initialize Window
root = Tk()
root.geometry("500x500")
root.title("REAL-TIME WEATHER APP")
root.configure(bg='#0A5171')

# Functions to fetch and display weather info
city_value = StringVar()

# Define weather function
def showWeather():
    api_key = "09f08f5104c25cfe447f87f39f1b0fbe"
    city_name = city_value.get()
    api = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(api)
    weather_info = response.json()

    if weather_info['cod'] == 200:
        kelvin = 273
        temp = int(weather_info['main']['temp'] - kelvin)
        pressure = weather_info['main']['pressure']
        wind_speed = weather_info['wind']['speed'] * 3.6
        humidity = weather_info['main']['humidity']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        # lower part - Interface
        Label(root, text=f"{temp}°C", font="Courier 65 bold", fg="White", bg='#0A5171', padx=47).place(x=80, y=55)
        Label(root, text=city_name, font="arial 20 bold", fg="White", bg='#0A5171', padx=100).place(x=80, y=140)
        Label(root, text=f"Pressure :                 {pressure} hPa", font="arial 14 bold", fg="White", bg='#0A5171', padx=100).place(x=0, y=210)
        Label(root, text=f"Wind speed :             {wind_speed} km/h", font="arial 14 bold", fg="White", bg='#0A5171', padx=100).place(x=0, y=260)
        Label(root, text=f"Humidity :                   {humidity}", font="arial 14 bold", fg="White", bg='#0A5171', padx=100).place(x=0, y=310)
        Label(root, text=f"Cloudy at :                 {cloudy}%", font="arial 14 bold", fg="White", bg='#0A5171', padx=100).place(x=0, y=360)
        Label(root, text=f"Currently :                 {description}", font="arial 14 bold", fg="White", bg='#0A5171', padx=100).place(x=0, y=410)
    else:
        messagebox.showwarning('Warning', 'Kindly enter valid city name!')

# upper part - Interface
Entry(root, textvariable=city_value, width='20', justify=CENTER, font='arian 17 bold').place(x=45, y=20)
Button(root, command=showWeather, text="Check Weather", activebackground='#145675', font="arial 13 bold", width=12, bg='#E1E1E3', fg ='Black', padx=5).place(x=315, y=20)
root.mainloop()
