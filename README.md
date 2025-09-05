# 🌦️ Real-Time Weather App

A simple **desktop weather application** built with **Python (Tkinter)** that fetches and displays real-time weather data using the **OpenWeatherMap API**.

## 📌 Features

* Get **real-time weather** updates by entering a city name.
* Displays:

  * 🌡️ Temperature (°C)
  * 🌬️ Wind Speed (km/h)
  * 💧 Humidity
  * ☁️ Cloud Coverage (%)
  * 🌀 Pressure (hPa)
  * 🌍 Weather Description
* User-friendly **Tkinter GUI** with a clean interface.
* Error handling for invalid city names.

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Install dependencies

Make sure you have **Python 3.x** installed, then run:

```bash
pip install requests
```

### 3. Get an OpenWeatherMap API Key

* Sign up at [OpenWeatherMap](https://openweathermap.org/)
* Generate a free API key.
* Replace the `api_key` in `Weather_app.py` with your own:

```python
api_key = "your_api_key_here"
```

### 4. Run the app

```bash
python Weather_app.py
```

## 📸 Screenshots

*(Optional: Add screenshots of your app here for better presentation.)*

## ⚙️ Tech Stack

* **Python 3**
* **Tkinter** (GUI)
* **Requests** (HTTP API calls)
* **OpenWeatherMap API**

## ❗ Notes

* Make sure you are connected to the internet for fetching weather data.
* If you enter an invalid city name, a warning will be shown.

## 📝 License

This project is open-source under the **MIT License**.

---
