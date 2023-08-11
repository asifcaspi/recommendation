from db import s3
from PIL import Image
import config
import io
from models.catsModel import predict, compare
from models.dogsModel import predict_breed_transfer, compare1

# image_object1 = s3.get_object(Bucket=config.BUCKET, Key='2.jpg')["Body"].read()
# image1 = Image.open(io.BytesIO(image_object1))
# image_object2 = s3.get_object(Bucket=config.BUCKET, Key='3.jpg')["Body"].read()
# image2 = Image.open(io.BytesIO(image_object2))
# cats stuff
# compare(predict(image1), predict(image2))
image_object1 = s3.get_object(Bucket=config.BUCKET, Key='bla1.jpg')["Body"].read()
image1 = Image.open(io.BytesIO(image_object1))
image_object2 = s3.get_object(Bucket=config.BUCKET, Key='bla2.jpg')["Body"].read()
image2 = Image.open(io.BytesIO(image_object2))
compare1(predict_breed_transfer(image1), predict_breed_transfer(image2))



