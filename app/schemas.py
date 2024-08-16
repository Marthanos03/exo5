from pydantic import BaseModel
from datetime import datetime


class BookingBase(BaseModel):
    """booking base colomn's database"""
    passenger_name: str
    flight_number: str
    departure: str
    destination: str
    date: datetime


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BookingBase):
    pass


class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True
