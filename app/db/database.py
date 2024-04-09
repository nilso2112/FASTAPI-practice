from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

#SQLAlCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/fastapi-database"
SQLAlCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLAlCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()