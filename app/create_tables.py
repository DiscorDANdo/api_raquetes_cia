# create_tables.py
from app.database_connect import Base, engine
from app.models import users, products, orders  # certifique-se de importar todos os modelos
from icecream import ic

Base.metadata.create_all(bind=engine)
ic("Tables created!")