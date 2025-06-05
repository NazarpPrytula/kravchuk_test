from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('postgres')}:{os.getenv('1234')}@{os.getenv('localhost')}:{os.getenv('5432')}/{os.getenv('dotastat')}"

engine = create_engine("postgresql://postgres:1234@localhost/dotastat")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
