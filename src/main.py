from config.db import s3
from models.catsModel import compare_cats
from models.dogsModel import compare_dogs
from models.sentenceModel import compare_sentences
from repository.sql import get_all_unadoppted_animals, get_all_users_likes
from repository.s3 import get_image_by_key
import pycron

# @pycron.cron("* * * * *")
def main(timestamp):
    user_likes = get_all_users_likes()
    animals = get_all_unadoppted_animals()
    print(len(animals))
    for user_like in user_likes:
        for animal in animals:
            if animal.id != user_like.animal.id:
                description_similarity = compare_sentences([user_like.animal.description, animal.description])


main(1)
# Run the scheduler continuously
# if __name__ == '__main__':
#     pycron.start()

# cats stuff
# print(compare_cats(get_image_by_key('1.jpg'), get_image_by_key('3.jpg'))) above 90
# dogs staff
# print(compare_dogs(get_image_by_key('4.jpg'), get_image_by_key('5.jpg'))) above 80



