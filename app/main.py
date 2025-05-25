from fastapi import FastAPI
from app.routers import users, products, orders

app = FastAPI()

# Inclui as rotas
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix='/products', tags=["Products"])
app.include_router(orders.router, prefix="/orders")