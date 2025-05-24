from sqlalchemy import Column, Integer, String
from app.database_connect import database_connect

db = database_connect()
Base = db.Base

class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    login = Column(String(255), unique=True, index=True)
    user_password = Column(String(255))