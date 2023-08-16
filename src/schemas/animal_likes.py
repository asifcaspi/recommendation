from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from config.db import Base

class AnimalLikes(Base):
    __tablename__ = 'animals_liked_by_user'

    animalsId = Column(String, ForeignKey('animal.id'), primary_key=True)
    animal = relationship("Animal", foreign_keys=[animalsId])
    userId = Column(String, ForeignKey('users.id'), primary_key=True)
    user = relationship("User", foreign_keys=[userId])