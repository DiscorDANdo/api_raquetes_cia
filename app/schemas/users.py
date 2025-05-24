from pydantic import BaseModel, EmailStr

# Cria usuários com email, login e senha
class UserCreate(BaseModel):
    email: EmailStr
    login: str
    password: str

# Faz login com login OU email e senha. Necessário fazer verificação se é login ou email no backend.
class UserLogin(BaseModel):
    identifier: str
    password: str

# Modelo de resposta do usuário.
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class config:
        orm_mode = True # Permite usar objetos ORM (como os do SQLAlchemy) diretamente