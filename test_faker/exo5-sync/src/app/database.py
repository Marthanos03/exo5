from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@db:5432/flight_booking_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(engine)


def get_db():
    """get the database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
