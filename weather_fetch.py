import requests

# Step 1: Define the url and parameters 
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "current_weather": True,
    "temperature_unit": "celsius"
}

# Step 2: Make the GET request to the API
response = requests.get(url, params=params, timeout=10)

# Step 3: Check the status before using the data
if response.status_code == 200:
    data = response.json()
    weather = data.get("current_weather")

    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind speed: {weather['windspeed']} km/h")
else:
    print(f"Error: {response.status_code}")
    print(response.text)