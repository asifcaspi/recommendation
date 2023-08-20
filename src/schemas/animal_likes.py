from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from config.db import Base

class AnimalLikes(Base):
    __tablename__ = 'animals_liked_by_user'

    animalsId = Column(String, ForeignKey('animals.id'), primary_key=True)
    animal = relationship("Animal", foreign_keys=[animalsId], lazy='joined')
    userId = Column(String, ForeignKey('user.id'), primary_key=True)
    user = relationship("User", foreign_keys=[userId], lazy='joined')