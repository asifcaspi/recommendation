from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime

class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    animal_id = Column(Integer, ForeignKey('animals.id'))
    animal = relationship("Animal", foreign_keys=[animal_id], lazy='joined')
    reason = Column(String)
    confidence = Column(Float)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", foreign_keys=[user_id], lazy='joined')

def create_recommendation(animal_id, reason, confidence, user_id):
    return Recommendation(animal_id=animal_id, reason=reason, confidence=confidence, user_id=user_id, date=datetime.now())