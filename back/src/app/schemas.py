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


class BookingPatch(BaseModel):
    passenger_name: str | None = None
    flight_number: str | None = None
    departure: str | None = None
    destination: str | None = None
    date: datetime | None = None


class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True
