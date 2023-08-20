from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from config.db import Base

class AnimalImages(Base):
    __tablename__ = 'animals_images'

    id = Column(String, primary_key=True, autoincrement=True)

    animalId = Column(String, ForeignKey('animals.id'))
    animal = relationship("Animal", foreign_keys=[animalId], lazy='joined', uselist=False)
    
    image = Column(String)