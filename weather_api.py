import requests

def fetch_coordinates(city, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city,
        'limit': 1,  # We only need the first matching result
        'appid': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            raise ValueError("City not found")
    else:
        response.raise_for_status()

def fetch_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
