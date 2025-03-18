import requests

API_KEY = 'ec2e16851814ab'
url = f"https://ipinfo.io/json?token={API_KEY}"

response = requests.get(url)
data = response.json()

#print(data)  # Prints the full location data


city = data['city']
#print(city)  # Prints the city name