from sqlalchemy import Column, Integer, String
from app.database_connect import Base

class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    login = Column(String(255), unique=True, index=True)
    password = Column(String(255))