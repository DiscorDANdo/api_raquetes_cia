from sqlalchemy import Column, Integer, String, Float
from app.database_connect import Base


class product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    category = Column(String(255), nullable=False, unique=False, index=True)
    value = Column(Float, nullable=False)