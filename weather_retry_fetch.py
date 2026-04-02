import requests
import time

def fetch_with_retry(url, params=None, mx_retries=3, delay=2):
    for attempt in range(1 , mx_retries + 1):
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 500:
                wait = int(response.headers.get("Retry-After", delay))
                print(f'rate limit hit, retrying after {wait} seconds...')
                time.sleep(wait)

            else:
                print(f"Error: {response.status_code}")
                return None
            

        except requests.exceptions.Timeout:
            print(f"Request timed out on attempt {attempt}. Retrying...")
            time.sleep(delay)
        except requests.exceptions.connectingError:
            print("Not internet connection. Please check your connection and try again.")
            return None
    print("Max retries reached. Failed to fetch data.")
    return None




# call the function
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "hourly": "temperature_2m",
    "current_weather": True
}
data = fetch_with_retry(url, params=params)

if data:
    print(data["current_weather"])
