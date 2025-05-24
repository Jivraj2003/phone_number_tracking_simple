# 📍 Simple Phone Number Tracker

A beginner-friendly Python program that tracks the **registered location**, **carrier**, and **geographic coordinates** of a phone number using the `phonenumbers` and `OpenCage Geocoder` APIs. The result is displayed on an interactive map using `folium`.

> ⚠️ Note: This tool does **not** track real-time location. It only provides the location where the number is originally registered.

---

## 🚀 Features

- Detects the **location** (e.g., Nepal)
- Identifies the **carrier/service provider** (e.g., Ncell, NTC)
- Converts the location into **latitude and longitude**
- Generates an **interactive map** (HTML file) showing the location

---

## 🛠 Requirements

Install the following Python libraries before running the script:

```bash
pip install phonenumbers
pip install opencage
pip install folium
