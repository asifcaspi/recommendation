import boto3
import psycopg2
import config

# Connect to Amazon S3
s3 = boto3.client('s3',
                  aws_access_key_id=config.ACCESS_KEY,
                  aws_secret_access_key=config.SECRET_KEY, 
                  region_name=config.REGION_NAME)
# Connect to PostgreSQL
# conn = psycopg2.connect(
#     host=config.HOST,
#     port=config.PORT,
#     database=config.DATABASE,
#     user=config.USERNAME,
#     password=config.PASSWORD
# )
# cur = conn.cursor()


# def close_connection():
#     cur.close()
#     conn.close()