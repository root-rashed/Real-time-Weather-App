<div align="center">


# 🌩️ Real-Time Weather App

### *Live atmospheric intelligence, right on your desktop*

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6B35?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-EB6E4B?style=for-the-badge&logo=openweathermap&logoColor=white)](https://openweathermap.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-00D4FF?style=for-the-badge)]()

<br>

> **"Your first API-powered application — where code meets the cloud, literally."**

</div>

---

## 🌐 Overview

**Real-Time Weather App** is a desktop application that pulls live atmospheric data from anywhere on Earth using the **OpenWeatherMap API** and presents it through a clean **Python Tkinter GUI**. This project marks a milestone — the first API integration built entirely in **VS Code**, bridging beginner Python skills with real-world web service consumption.

Type a city. Hit enter. Get the sky's current status — instantly.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🌡️ **Temperature** | Real-time temperature in Celsius |
| 🌬️ **Wind Speed** | Current wind speed in km/h |
| 💧 **Humidity** | Atmospheric moisture percentage |
| ☁️ **Cloud Coverage** | Sky cloud cover in percentage |
| 🌀 **Pressure** | Atmospheric pressure in hPa |
| 🌍 **Weather Description** | Human-readable sky condition |
| ⚠️ **Error Handling** | Smart alerts for invalid city names |

---

## ⚙️ Tech Stack

```
┌─────────────────────────────────────────────────┐
│                  ARCHITECTURE                   │
├─────────────────────┬───────────────────────────┤
│  Language           │  Python 3.x               │
│  GUI Framework      │  Tkinter                  │
│  HTTP Client        │  Requests                 │
│  Data Source        │  OpenWeatherMap REST API  │
│  IDE                │  VS Code                  │
└─────────────────────┴───────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your machine.

```bash
python --version
```

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/root-rashed/Real-time-Weather-App.git
cd Real-time-Weather-App
```

### 2️⃣ Install Dependencies

```bash
pip install requests
```

> `tkinter` comes pre-installed with Python. No extra install needed.

### 3️⃣ Get Your API Key

1. Visit 👉 [https://openweathermap.org/](https://openweathermap.org/)
2. Create a **free account**
3. Navigate to **API Keys** in your dashboard
4. Copy your key

### 4️⃣ Configure the App

Open `main.py` in VS Code and replace the placeholder:

```python
# main.py
api_key = "your_api_key_here"   # ← Paste your key here
```

### 5️⃣ Launch the App

```bash
python main.py
```

> A GUI window will open. Enter any city name and fetch live weather data instantly. 🎯

---

## 📁 Project Structure

```
Real-time-Weather-App/
│
├── main.py          # Core application logic + GUI
└── README.md        # Project documentation
```

---

## 🔮 Roadmap — Future Enhancements

- [ ] 🌙 Dark / Light theme toggle
- [ ] 📍 Auto-detect location via IP geolocation
- [ ] 📅 5-day weather forecast view
- [ ] 🗺️ Interactive world map integration
- [ ] 🔔 Weather alerts and notifications
- [ ] 📊 Temperature trend graphs with Matplotlib
- [ ] 🌐 Multi-language support

---

## ⚠️ Important Notes

- An active **internet connection** is required for API calls.
- The free tier of OpenWeatherMap allows **60 calls/minute** — more than enough for personal use.
- Never share or hard-code your API key in public repositories. Consider using a `.env` file for production setups.

---

## 🧠 What I Learned

> This project was my **first hands-on experience** with external APIs — understanding how to make HTTP requests, parse JSON responses, and render live data inside a Python GUI. Built entirely in **VS Code**, it taught me the complete workflow from environment setup to shipping a working desktop app.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

```
MIT License © 2025 root-rashed
```

---

## 🌟 Connect

<div align="center">

If this project helped you or you found it interesting — drop a ⭐ on the repo. It means a lot!

[![GitHub](https://img.shields.io/badge/GitHub-root--rashed-181717?style=for-the-badge&logo=github)](https://github.com/root-rashed)

---

*Built with curiosity, caffeine, and a free API key* ☕

</div>
