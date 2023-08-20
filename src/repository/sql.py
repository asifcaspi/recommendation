from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.orm.exc import NoResultFound
from config.db import sql_engine
from schemas.animal_likes import AnimalLikes
from schemas.user import User
from schemas.animal import Animal
from schemas.recommendation import Recommendation
from schemas.animal_images import AnimalImages

def get_image_from_animal_image(animal_image):
    return animal_image.image

def set_only_images(animal):
    animal.string_images = list(map(get_image_from_animal_image, animal.images))
    return animal

def set_images_empty(animal):
    animal.string_images = []
    return animal


def get_all_unadoppted_animals():
    Session = sessionmaker(bind=sql_engine)
    session = Session()

    try:
        # Querying for animal with taken_by as undefined (NULL)
        animal_images_alias = aliased(AnimalImages)

        unadopted_animals = session.query(Animal).filter(
            Animal.taken_by == None).join(AnimalImages).all()
        animals_without_images = (
            session.query(Animal)
            .outerjoin(animal_images_alias, Animal.id == animal_images_alias.animalId)
            .filter(Animal.taken_by == None, animal_images_alias.id == None)
            .all()
        )

        return list(map(set_only_images, unadopted_animals)) + list(map(set_images_empty, animals_without_images))

    except NoResultFound:
        return []

    finally:
        session.close()


def get_all_users_likes():
    Session = sessionmaker(bind=sql_engine)
    session = Session()

    try:
        likes = session.query(AnimalLikes).all()

        return likes

    except NoResultFound:
        return []

    finally:
        session.close()


def insert_recommendations(recommendations_data):
    Session = sessionmaker(bind=sql_engine)
    session = Session()
    try:
        for data in recommendations_data:
            # Add to session and commit
            session.add(data)
        session.commit()
        print("Recommendations inserted successfully!")

    except Exception as e:
        session.rollback()

    finally:
        session.close()
