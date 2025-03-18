# Weather Forecast App

## Overview

This is a simple Python-based weather forecast application that retrieves and displays the current weather, a 5-day forecast, and an optional temperature graph for the next 24 hours. The app uses the OpenWeatherMap API to fetch weather data and the IPInfo API to determine the user's location.

## Features

- Automatically detects the user's city using IPInfo.
- Retrieves and displays the current weather conditions.
- Provides a 5-day weather forecast (midday temperatures only).
- Offers a graphical representation of temperature changes for the next 24 hours.
- Allows users to check the weather for additional cities.

## Technologies Used

- Python
- OpenWeatherMap API
- IPInfo API
- Matplotlib (for graphing)
- Requests (for API calls)

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

You also need to install the required Python libraries. Run the following command:

```sh
pip install requests matplotlib
```

### API Keys

You need API keys for OpenWeatherMap and IPInfo:

1. **OpenWeatherMap API**: Sign up at [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
2. **IPInfo API**: Get a free token from [IPInfo](https://ipinfo.io/).

Store your OpenWeatherMap API key in `api.py`:

```python
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
```

Replace `API_KEY` in `location.py` with your IPInfo token:

```python
API_KEY = "YOUR_IPINFO_API_KEY"
```

## Usage

Run the program using:

```sh
python app.py
```

The app will:

1. Detect your current city.
2. Display the current weather and a 5-day forecast.
3. Ask if you want to view a temperature graph for the next 24 hours.
4. Allow you to check the weather for other cities.

## File Structure

```
weather-app/
│── app.py            # Main application logic
│── api.py            # Stores API key for OpenWeatherMap
│── location.py       # Determines user location using IPInfo
│── weather_graph.py  # Generates a temperature graph
│── README.md         # Project documentation
```

## Future Improvements

- Add support for more weather details (e.g., wind direction, pressure, UV index).
- Improve error handling for API failures.
- Implement a GUI version using Tkinter or PyQt.
- Cache results to reduce API calls.

## License

This project is open-source and available under the MIT License.


