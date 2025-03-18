import requests
import matplotlib.pyplot as plt
from datetime import datetime
from location import city
from api import api_key

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric")
forecast_data = response.json()

# Extract the forecast data
temps_first_24_hours = {}

for entry in forecast_data["list"][:8]:  # First 24 hours
    date = entry["dt_txt"]
    temperature = entry["main"]["temp"]
    temps_first_24_hours[date] = temperature

print(temps_first_24_hours)