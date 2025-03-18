import requests

api_key = "d01647675b2bb6d5e9c542cfcbbe1ff6"

city = input("Enter city name: ")
#city = "London"

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



