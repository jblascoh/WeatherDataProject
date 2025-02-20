import sys
import requests
import pandas as pd
from constants import OPENWEATHER_API_KEY, BASE_URL


def connect_weather() -> str:   #conecta con la api de openweather
    try:
        api_key = OPENWEATHER_API_KEY
        if api_key:
            print("Successfully connected to OpenWeather!")
            return api_key
        else:
            print("API key not found!")
            sys.exit(1)
    except Exception as e:
        print(f"Error connecting to OpenWeather: {e}")
        sys.exit(1)


def extract_weather_data(city: str, api_key: str):  #solicitud a la api para extraer datos 

    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def formato_numero(value):
    return value if isinstance(value, (int, float)) else 0

def formato_texto(value):
    return value if isinstance(value, str) else "Unknown"

def transform_data(weather_data):   #validación y transformación de los datos
    
    weather_list = []
    for entry in weather_data['list']:
        weather_info = {
            'datetime': formato_texto(entry.get('dt_txt', "Unknown")),
            'temperature': formato_numero(entry['main'].get('temp', 0)),
            'feels_like': formato_numero(entry['main'].get('feels_like', 0)),
            'min_temp': formato_numero(entry['main'].get('temp_min', 0)),
            'max_temp': formato_numero(entry['main'].get('temp_max', 0)),
            'pressure': formato_numero(entry['main'].get('pressure', 0)),
            'humidity': formato_numero(entry['main'].get('humidity', 0)),
            'weather_main': formato_texto(entry['weather'][0].get('main', "Unknown")),
            'cloud_cover': formato_numero(entry['clouds'].get('all', 0)),
            'wind_speed': formato_numero(entry['wind'].get('speed', 0)),
            'wind_deg': formato_numero(entry['wind'].get('deg', 0)),
            'wind_gust': formato_numero(entry['wind'].get('gust', 0)),
            'visibility': formato_numero(entry.get('visibility', 0)),
            'pop': formato_numero(entry.get('pop', 0))
        }
        weather_list.append(weather_info)
        
    df = pd.DataFrame(weather_list)
    return df


def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)
