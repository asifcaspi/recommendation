from utils.cron_decorator import scheduled_task
from config.db import s3
from models.catsModel import predict, compare
from models.dogsModel import predict_breed_transfer, compare1
from repository.sql import get_all_unadoppted_animals, get_all_users_likes
import schedule
import time

@scheduled_task(cron_expression="* * * * *")
def main():
    print('workssss')
    print('sdfdsfdsfsd' + get_all_users_likes())

# Run the scheduler continuously
while True:
    schedule.run_pending()
    time.sleep(1)

# image_object1 = s3.get_object(Bucket=config.BUCKET, Key='2.jpg')["Body"].read()
# image1 = Image.open(io.BytesIO(image_object1))
# image_object2 = s3.get_object(Bucket=config.BUCKET, Key='3.jpg')["Body"].read()
# image2 = Image.open(io.BytesIO(image_object2))
# cats stuff
# compare(predict(image1), predict(image2))
# dogs staff
# image_object1 = s3.get_object(Bucket=config.BUCKET, Key='bla1.jpg')["Body"].read()
# image1 = Image.open(io.BytesIO(image_object1))
# image_object2 = s3.get_object(Bucket=config.BUCKET, Key='bla2.jpg')["Body"].read()
# image2 = Image.open(io.BytesIO(image_object2))
# compare1(predict_breed_transfer(image1), predict_breed_transfer(image2))



