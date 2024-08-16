from sqlalchemy.orm import Session
from . import models, schemas


def get_booking(db: Session, booking_id: int):
    """get a booking with an ID"""
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()


def get_bookings(db: Session):
    """get all bookings"""
    return db.query(models.Booking).all()


def create_booking(db: Session, booking: schemas.BookingCreate):
    """create a new booking"""
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def update_booking(db: Session, booking_id: int, booking: schemas.BookingUpdate):
    """update a booking with an ID"""
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if db_booking:
        for key, value in booking.dict().items():
            setattr(db_booking, key, value)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    return None


def delete_booking(db: Session, booking_id: int):
    """delete a booking with an ID"""
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
        return db_booking
    return None
