from sqlalchemy.orm import Session
from src.app import models, schemas
from src.app.exceptions import BookingNotFoundException


def get_booking(db: Session, booking_id: int) -> schemas.Booking:
    """get a booking with an ID"""
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise BookingNotFoundException(booking_id)
    return booking


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
    if not db_booking:
        raise BookingNotFoundException(booking_id)
    for key, value in booking.dict().items():
        setattr(db_booking, key, value)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def patch_booking(db: Session, booking_id: int, booking: schemas.BookingPatch):
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not db_booking:
        raise BookingNotFoundException(booking_id)
    for key, value in booking.dict().items():
        if key and value is not None:
            setattr(db_booking, key, value)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def delete_booking(db: Session, booking_id: int):
    """delete a booking with an ID"""
    db_booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not db_booking:
        raise BookingNotFoundException(booking_id)
    db.delete(db_booking)
    db.commit()
    return db_booking
