from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.orm.exc import NoResultFound
from config.db import sql_engine
from schemas.animal_likes import AnimalLikes
from schemas.user import User
from schemas.animal import Animal
from schemas.recommendation import Recommendation
from schemas.animal_images import AnimalImages


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

        return unadopted_animals + animals_without_images

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
            # Extract data for each recommendation
            post_id = data['post_id']
            user_id = data['user_id']
            reason = data['reason']
            confidence = data['confidence']

            # Create Recommendation instance
            recommendation = Recommendation(
                post_id=post_id,
                user_id=user_id,
                reason=reason,
                confidence=confidence
            )

            # Add to session and commit
            session.add(recommendation)
        session.commit()
        print("Recommendations inserted successfully!")

    except Exception as e:
        session.rollback()
        print("Error:", e)

    finally:
        session.close()
