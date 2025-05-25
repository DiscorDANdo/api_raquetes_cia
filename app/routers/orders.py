from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import orders as order_schema
from app.models import orders as order_model
from app.database_connect import SessionLocal

router = APIRouter()


def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@router.post("/", response_model=order_schema.order)
def create_order(order: order_schema.orderCreate, db: Session = Depends(get_db)):
    db_order = order_model.order(**order.dict)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=list[order_schema.order])
def list_orders(db: Session = Depends(get_db)):
    return db.query(order_model.order).all()

@router.get("/{order_id}", response_model=order_schema.order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(order_model.order).filter(order_model.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order