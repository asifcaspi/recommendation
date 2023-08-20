import os
from dotenv import load_dotenv
load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY_ID')
SECRET_KEY = os.getenv('SECRET_ACCESS_KEY')
HOST = os.getenv('PGSQL_HOST')
PORT = 5432
DATABASE = os.getenv('PGSQL_DATABASE')
PASSWORD = os.getenv('PGSQL_PASSWORD')
USERNAME = os.getenv('PGSQL_USERNAME')
BUCKET = os.getenv('BUCKET')
REGION_NAME = 'eu-central-1'