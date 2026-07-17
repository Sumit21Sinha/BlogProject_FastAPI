from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url is None:
    raise ValueError("DATABASE_URL not found in .env")

engine = create_engine(database_url, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()