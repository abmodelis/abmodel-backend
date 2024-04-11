from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.env import Env

engine = create_engine(Env.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
