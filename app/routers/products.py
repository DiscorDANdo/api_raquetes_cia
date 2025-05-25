from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import products as product_schema
from app.models import products as product_model
from app.database_connect import SessionLocal

router = APIRouter()

def get_db():
    db_session = SessionLocal()

    try:
        yield db_session
    finally:
        db_session.close()

@router.post("/", response_model=product_schema.ProductResponse)
def create_product(product: product_schema.ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(product_model.product).filter(product_model.product.name == product.name).first()
    if db_product:
        raise HTTPException(status_code=400, detail="Product already exists.")
    
    new_product = product_model.product(
        name=product.name,
        category=product.category,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.get("/list", response_model=list[product_schema.ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(product_model.product).all()