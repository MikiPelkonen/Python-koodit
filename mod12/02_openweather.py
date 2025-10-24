import requests

PROMPT_TEXT: str = "Enter municipality name: "
API_KEY: str = "eb63093eff50f4009b7cba745bbe3d7e"


def fetch_coordinates(municipality: str) -> tuple[float, float]:
    coords_request_url = f"https://api.openweathermap.org/geo/1.0/direct?q={municipality}&limit=1&appid={API_KEY}"
    try:
        response = requests.get(coords_request_url)
        response.raise_for_status()
        coords_data = response.json()
        if not coords_data:
            raise ValueError(f"No data found for municipality: {municipality}")
        return float(coords_data[0]["lat"]), float(coords_data[0]["lon"])

    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Request exception: {e}")
    except ValueError as e:
        raise SystemExit(f"Missing data: {e}")


def fetch_weather(lat: float, lon: float) -> tuple[str, float]:
    weather_request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    try:
        response = requests.get(weather_request_url)
        response.raise_for_status()
        weather_data = response.json()
        if not weather_data:
            raise ValueError(f"No weather data found for coords Lat: {lat} Lon: {lon}")
        return weather_data["weather"][0]["description"], float(
            weather_data["main"]["temp"]
        )
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Request exception: {e}")
    except ValueError as e:
        raise SystemExit(f"Missing data: {e}")


municipality = input(PROMPT_TEXT).strip()

try:
    lat, lon = fetch_coordinates(municipality)
    weather = fetch_weather(lat, lon)
    print(f"Weather: {weather[0].capitalize()}")
    print(f"Temperature: {weather[1]} Celsius")
except SystemExit as e:
    print(f"{e}")
    print("Exiting gracefully...")
