from fastapi import FastAPI, HTTPException
from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/booking/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate):
    """endpoint to create a booking"""
    db = get_db()
    res = crud.create_booking(db, booking)
    db.close()
    return res


@app.get("/booking/", response_model=list[schemas.Booking])
def read_bookings():
    """endpoint to get all bookings"""
    db = get_db()
    bookings = crud.get_bookings(db)
    db.close()
    return bookings


@app.get("/booking/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: int):
    """endpoint to get a booking by ID"""
    db = get_db()
    db_booking = crud.get_booking(db, booking_id=booking_id)
    db.close()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking


@app.put("/booking/{booking_id}", response_model=schemas.Booking)
def update_booking(booking_id: int, booking: schemas.BookingUpdate):
    """endpoint to update a booking"""
    db = get_db()
    db_booking = crud.update_booking(db, booking_id, booking)
    db.close()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking


@app.delete("/booking/{booking_id}", response_model=schemas.Booking)
def delete_booking(booking_id: int):
    """endpoint to delete a booking"""
    db = get_db()
    db_booking = crud.delete_booking(db, booking_id=booking_id)
    db.close()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking
