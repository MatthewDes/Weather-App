import requests
import matplotlib.pyplot as plt
#from location import city
from api import api_key


def make_graph(city):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric")
    forecast_data = response.json()

    # Extract the forecast data for next 24 hours
    temps_first_24_hours = {}

    for entry in forecast_data["list"][:8]:  # First 24 hours
        time = entry["dt_txt"].split(" ")[1]
        temperature = entry["main"]["temp"]
        temps_first_24_hours[time] = temperature

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(list(temps_first_24_hours.keys()), list(temps_first_24_hours.values()), marker='o')
    plt.title(f"Temperature forecast for the next 24 hours in {city}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# print(temps_first_24_hours)
# make_graph()