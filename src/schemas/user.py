from sqlalchemy import Column, Integer, String
from config.db import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True, autoincrement=True)
    user_name = Column(String)
    email = Column(String)
    image_url = Column(String)
    age = Column(Integer)
    description = Column(String)  