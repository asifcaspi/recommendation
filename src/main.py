from config.db import s3
from models.catsModel import compare_cats
from models.dogsModel import compare_dogs
from models.sentenceModel import compare_sentences
from repository.sql import get_all_unadoppted_animals, get_all_users_likes, insert_recommendations
from repository.s3 import get_image_by_key
from constants.dogs import min_dogs_similarity
from constants.cats import min_cats_similarity
from constants.sentence import min_sentences_similarity
from constants.reasons import description_similarity_reason, image_similarity_reason
from schemas.recommendation import create_recommendation
import pycron

@pycron.cron("0 0 * * *")
def main(timestamp):
    user_likes = get_all_users_likes()
    animals = get_all_unadoppted_animals()
    recommendations = []

    for user_like in user_likes:
        for animal in animals:
            if animal.id != user_like.animal.id:
                description_similarity = compare_sentences([user_like.animal.description, animal.description])
                images = [animal.image, *animal.string_images]
                liked_animal_image = user_like.animal.image
                image_similarity_sum = 0
                if description_similarity > min_sentences_similarity:
                    recommendations.append(
                        create_recommendation(animal.id, description_similarity_reason, description_similarity, user_like.userId))
                else:
                    for image in images:
                        image_to_compare1, image_to_compare2 = get_image_by_key(liked_animal_image), get_image_by_key(image)
                        if animal.category_name == 'cat':
                            image_similarity_sum += compare_cats(image_to_compare1, image_to_compare2)
                        elif animal.category_name == 'dog':
                            image_similarity_sum += compare_dogs(image_to_compare1, image_to_compare2)
                    avg_image_similarity = image_similarity_sum / len(images)
                    if (animal.category_name == 'cat' and avg_image_similarity > min_cats_similarity) or avg_image_similarity > min_dogs_similarity:
                        avg_image_similarity = float(avg_image_similarity)
                        recommendations.append(
                            create_recommendation(animal.id, image_similarity_reason, avg_image_similarity, user_like.userId))
    insert_recommendations(recommendations_data=recommendations)


# Run the scheduler continuously
if __name__ == '__main__':
    pycron.start()



