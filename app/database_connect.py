from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from icecream import ic
from dotenv import load_dotenv
import mysql.connector
import pandas as pd
import os

load_dotenv()

db_user = os.getenv("user")
db_password = os.getenv("password")
db_host = os.getenv("host")
db_port = os.getenv("port")
dbname = os.getenv("dbname")

# Connection with mysql.connector
connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=dbname
)
cursor = connection.cursor()

# Connection with SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
    
    # def close_con(self):
    #     # Close the database connection
    #     self.cursor.close()
    #     self.connection.close()
    #     ic("Connection closed.")

    # def execute_query(self, query: str):
    #     try:
    #         if query.strip().lower().startswith("select"):
    #             self.cursor.execute(query)

    #             if self.cursor.description is not None:
    #                 return self.cursor.fetchall()
    #             else:
    #                 ic("No data found.")
    #                 return []

    #         else:
    #             self.cursor.execute(query)
    #             self.connection.commit()

    #     except Exception as e:
    #         raise Exception(f'Query "{query}" inválida. Erro: {e}.')
    
    # def insert_data(self, data: pd.DataFrame, table_name: str) -> str:
    #     try:
    #         df = pd.DataFrame(data)
            
    #         df.to_sql(
    #             name=table_name,
    #             con=self.engine,
    #             if_exists='append', 
    #             index=False
    #             )
            
    #         return {"message":"Data inserted successfully!"}, data

    #     except Exception as e:
    #         raise Exception(f"Failed to insert data: {e}")
