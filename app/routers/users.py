from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

from app.schemas import users as user_schema
from app.models import users as user_model
from app.database_connect import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Configurações do JWT
load_dotenv()

SECRET_KEY = os.getenv("secret_key")
ALGORITHM = os.getenv("algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("access_token_expire_minutes"))

# Criptografia da senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

# Chama uma rota POST em que o usuário vai passar os dados
@router.post("/register", response_model=user_schema.UserResponse)
def register_user(user: user_schema.UserCreate, db: Session = Depends(get_db)): # Puxa o schema criado em user_schema
    db_user = db.query(user_model.user).filter(user_model.user.email == user.email).first() # Verifica se o email já está no db e retorna o primeiro valor

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered!") # Se o email já existir lança um HTTPException com status 400
    
    hashed_password = pwd_context.hash(user.password)
    new_user = user_model.user(email=user.email, login=user.login, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(user_model.user).filter(
        or_(
            user_model.user.email == user.identifier,
            user_model.user.login == user.identifier
        )
    ).first()

    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials!")
    
    access_token = create_access_token(data={"sub": db_user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}