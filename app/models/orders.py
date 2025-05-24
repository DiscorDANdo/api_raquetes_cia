from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from app.database_connect import database_connect

db = database_connect()

class order(db.Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    quantity = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())