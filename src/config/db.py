import boto3
import psycopg2
from sqlalchemy import create_engine
import config.config as config
from sqlalchemy.ext.declarative import declarative_base

# Connect to Amazon S3
s3 = boto3.client('s3',
                  aws_access_key_id=config.ACCESS_KEY,
                  aws_secret_access_key=config.SECRET_KEY, 
                  region_name=config.REGION_NAME)

# Connect to PostgreSQL
Base = declarative_base()
postgres_conn_string = f'postgresql://{config.USERNAME}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.DATABASE}'
sql_engine = create_engine(postgres_conn_string)
# conn = psycopg2.connect(
#     host=config.HOST,
#     port=config.PORT,
#     database=config.DATABASE,
#     user=config.USERNAME,
#     password=config.PASSWORD
# )
# cur = conn.cursor()