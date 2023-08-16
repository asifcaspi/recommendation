from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base

class Animal(Base):
    __tablename__ = 'animals'

    id = Column(String, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    category_name = Column(String)
    image = Column(String)
    sex = Column(String)
    age = Column(Integer)

    # Adding relationships to User model
    uploadedById = Column(String, ForeignKey('users.id'))
    uploaded_by = relationship("User", foreign_keys=[uploadedById])

    takenById = Column(String, ForeignKey('users.id'))
    taken_by = relationship("User", foreign_keys=[takenById])