from weather_etl import connect_weather, extract_weather_data, transform_data, load_data_to_csv
from constants import OUTPUT_PATH, INPUT_PATH
import pandas as pd

def weather_pipeline(file_name: str, city: str):

    api_key = connect_weather() #conectar a api

    if api_key:
        weather_data = extract_weather_data(city, api_key)   #extraer datos
        input_file_path = f"{INPUT_PATH}/{file_name}.csv"   #guardar datos de entrada
        input_data = pd.DataFrame([weather_data])
        load_data_to_csv(input_data, input_file_path)

        weather_df = transform_data(weather_data)   #transformar datos

        output_file_path = f"{OUTPUT_PATH}/{file_name}.csv"    #guardar datos de salida
        load_data_to_csv(weather_df, output_file_path)

        return output_file_path
    else:
        print("Failed to connect to OpenWeather.")
        return None
