import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

OPENWEATHER_API_KEY = parser.get('api_keys', 'openweather_api_key').strip('[]')
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USER = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id').strip('[]')
AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key').strip('[]')
AWS_REGION = parser.get('aws', 'aws_region').strip('[]')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name').strip('[]')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')