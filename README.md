# Smart Weather Assistant

## 📌 Overview

The **Smart Weather Assistant** is a command-line utility built in Python that delivers localized, real-time weather analytics and structured 5-day forecasts. By integrating with the OpenWeather API, the system goes beyond raw data aggregation to translate environmental metrics into actionable lifestyle recommendations.

### The Problem It Solves

Raw weather data is often fragmented or detached from daily human needs. Standard weather apps inundate users with figures (such as hectopascals or wind velocity) without contextualizing what those numbers mean for their immediate routine. This assistant bridges that gap by interpreting live metrics into direct actionable advice.

### Why It Is Useful

* **Intelligent Location Parsing:** It handles ambiguous location names by presenting multiple geographic candidates, allowing you to choose the exact city, state, and country you intend to look up.
* **Smart Contextual Advice:** It analyzes local temperatures and systemic weather conditions to generate dynamic recommendations regarding clothing choices and safety precautions.

---

## ⚡ Features

* **Interactive Geocoding Resolution:** Resolves user-entered city names into a list of up to 5 matching geographic locations (displaying City, State, and Country) using OpenWeather's Geocoding API to prevent ambiguous lookups.
* **Real-Time Current Metrics:** Captures localized temperature, perceived ("feels like") temperature, humidity levels, atmospheric pressure, wind speeds, and exact visibility ranges.
* **Dynamic Timezone Localization:** Automatically converts UTC sunrise and sunset timestamps into the exact local time of the queried target city using real-time timezone offsets.
* **5-Day Forecasting:** Aggregates extended forecasting data and filters outputs to deliver a clean mid-day summary for upcoming dates which can further be modified for 3-hours, 5-days forecasting.
* **Rule-Based Recommendation Engine:** Employs situational algorithms to output clothing recommendations based on thermal tiers and weather alerts (e.g., advising umbrellas for rain or warning against outdoor activities during thunderstorms).

---

## 🛠️ Tech Stack

### Frontend

* **Command Line Interface (CLI):** Built entirely using Python's native standard I/O streams for a distraction-free, zero-dependency visual interface.

### Backend

* **Python:** Written in modular, highly clean Python code leveraging functional decomposition.
* **HTTP Client:** Driven by the `requests` library to handle network transactions and external API handshakes.

### Database

* **Stateless Architecture:** No standalone local or cloud database required; values are fetched on-demand, processed in-memory, and localized directly on the fly.

### APIs / Integrations

* **OpenWeather Geocoding API:** Used to resolve string query parameters into precise latitude and longitude coordinates.
* **OpenWeather Current Weather Data API:** Powers the instantaneous situational reporting engine.
* **OpenWeather 5-Day Weather Forecast API:** Feeds the future multi-day predictive data blocks.
