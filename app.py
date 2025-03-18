import requests
from location import city 
from api import api_key
from weather_graph import make_graph


def get_weather(city):

    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric').json()

    #print(weather_data)
    weather = weather_data['weather'][0]['description']
    if weather == "clear sky":
        weather = "clear skies"
    elif weather == "few clouds":
        weather = "a few clouds"
    temperature = weather_data['main']['temp']
    temp_low = weather_data['main']['temp_min']
    temp_high = weather_data['main']['temp_max']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"""
      Today in {city} you can expect {weather}.
      The temperature is {temperature}°C with a low of {temp_low}°C and a high of {temp_high}°C.
      The humidity is {humidity}% and the wind speed is {wind_speed}m/s.
      """)

def get_5_day_forecast(city):
    forecast_data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric").json()
    daily_forecast = {}
    for entry in forecast_data["list"]:
        date = entry["dt_txt"].split(" ")[0]  # Extract date (YYYY-MM-DD)
        time = entry["dt_txt"].split(" ")[1]  # Extract time (HH:MM:SS)
        
        if time == "12:00:00":  # Get midday forecast for each day
            weather = entry["weather"][0]["description"]
            temperature = entry["main"]["temp"]
            #temp_min = entry["main"]["temp_min"]
            #temp_max = entry["main"]["temp_max"]
            
            daily_forecast[date] = {"weather": weather, "temperature": temperature}
            #daily_forecast[date] = {"weather": weather, "temp low": temp_min, "temp high": temp_max}

    print(f"\n5-Day Weather Forecast for {city}:")
    for date, info in daily_forecast.items():
        print(f"{date}: {info['weather']}, {info['temperature']}°C")
    print("\n")

def display_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
    test = response.json()
    if response.status_code != 200:  # If the city is not found
        print(f"Error: {test['message'].capitalize()}. Please enter a valid city.")
        return False
    
    get_weather(city)
    get_5_day_forecast(city)
    
def ask_graph(): 
    question = input("Would you like to see a graph of the temperature for the next 24 hours? (yes/no): ").strip().lower()
    if question == "yes":
        make_graph(city)




display_weather(city)
ask_graph()

#ask user if they want to find out the weather for another city
while True:
    question = input("Would you like to find out the weather for another city? (yes/no): ").strip().lower()
    if question != "yes":
        print("Thank you for using the weather app!")
        break
    city = input("Enter city name: ").strip().title()
    display_weather(city)
    ask_graph()
    

