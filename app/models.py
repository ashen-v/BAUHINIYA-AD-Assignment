from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=False)
    phone1 = Column(Integer, nullable=False)
    phone2 = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)
    password = Column(String, nullable=False)