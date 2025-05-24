from pydantic import BaseModel
from datetime import datetime

class orderBase(BaseModel):
    product_id: int
    user_id: int
    quantity: int

class orderCreate(orderBase):
    pass

class order(orderBase):
    id: int
    created_at: datetime

    class config:
        orm_mode = True
        