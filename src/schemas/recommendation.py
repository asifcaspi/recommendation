from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from config.db import Base

class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(String, ForeignKey('animals.id'))
    animal = relationship("Animal", foreign_keys=[animal_id])
    reason = Column(String)
    confidence = Column(Float)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship("User", foreign_keys=[user_id])