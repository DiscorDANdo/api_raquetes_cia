from fastapi import FastAPI
from app.routers import users, products, orders
from app.database_connect import database_connect

# TODO: Criar schemas, models e routers do orders
# TODO: Fazer testes dos schemas, models e routers

# Cria as tabelas
db = database_connect()

db.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

# Inclui as rotas
app.include_router(users.router, prefix="/users")
app.include_router(products.router, prefix='/products')
app.include_router(orders.router, prefix="/orders")