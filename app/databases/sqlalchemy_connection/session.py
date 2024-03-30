import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DB_URL = os.environ.get("DATABASE_URL")

if SQLALCHEMY_DB_URL is None:
    raise Exception("DATABASE_URL is not set")

engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
