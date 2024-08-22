import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Booking(Base):
    """booking database"""
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    passenger_name = Column(String, index=True)
    flight_number = Column(String, index=True)
    departure = Column(String, index=True)
    destination = Column(String, index=True)
    date = Column(DateTime(timezone=True), default=datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
