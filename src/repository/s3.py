from config.db import s3
import config.config as config
from PIL import Image
import io

def get_image_by_key(key):
    image_object = s3.get_object(Bucket=config.BUCKET, Key=key)["Body"].read()
    image = Image.open(io.BytesIO(image_object))

    return image