from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.app import schemas, crud
from src.app.database import get_db

router = APIRouter(prefix="/booking", tags=["booking"])


@router.post("/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    """endpoint to create a booking"""
    res = crud.create_booking(db, booking)
    return res


@router.get("/", response_model=list[schemas.Booking])
def read_bookings(db: Session = Depends(get_db)):
    """endpoint to get all bookings"""
    bookings = crud.get_bookings(db)
    return bookings


@router.get("/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    """endpoint to get a booking by ID"""
    db_booking = crud.get_booking(db, booking_id=booking_id)
    return db_booking


@router.put("/{booking_id}")
def update_booking(booking_id: int, booking: schemas.BookingUpdate, db: Session = Depends(get_db)) -> schemas.Booking:
    """endpoint to update a booking"""
    db_booking = crud.update_booking(db, booking_id, booking)
    return db_booking


@router.patch("/{booking_id}")
def patch_booking(booking_id: int, booking: schemas.BookingPatch, db: Session = Depends(get_db)) -> schemas.Booking:
    """endpoint to patch a booking"""
    db_booking = crud.patch_booking(db, booking_id, booking)
    return db_booking


@router.delete("/{booking_id}", response_model=schemas.Booking)
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    """endpoint to delete a booking"""
    db_booking = crud.delete_booking(db, booking_id=booking_id)
    return db_booking
