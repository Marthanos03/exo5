from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app import schemas, crud
from src.app.database import get_db

router = APIRouter(prefix="/booking", tags=["booking"])


@router.post("/", response_model=schemas.Booking)
async def create_booking(booking: schemas.BookingCreate, db: AsyncSession = Depends(get_db)):
    """endpoint to create a booking"""
    res = await crud.create_booking(db, booking)
    return res


@router.get("/", response_model=list[schemas.Booking])
async def read_bookings(db: AsyncSession = Depends(get_db)):
    """endpoint to get all bookings"""
    bookings = await crud.get_bookings(db)
    return bookings


@router.get("/{booking_id}", response_model=schemas.Booking)
async def read_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    """endpoint to get a booking by ID"""
    db_booking = await crud.get_booking(db, booking_id=booking_id)
    return db_booking


@router.put("/{booking_id}")
async def update_booking(booking_id: int, booking: schemas.BookingUpdate, db: AsyncSession = Depends(get_db)) -> schemas.Booking:
    """endpoint to update a booking"""
    db_booking = await crud.update_booking(db, booking_id, booking)
    return db_booking


@router.patch("/{booking_id}")
async def patch_booking(booking_id: int, booking: schemas.BookingPatch, db: AsyncSession = Depends(get_db)) -> schemas.Booking:
    """endpoint to patch a booking"""
    db_booking = await crud.patch_booking(db, booking_id, booking)
    return db_booking


@router.delete("/{booking_id}", response_model=schemas.Booking)
async def delete_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    """endpoint to delete a booking"""
    db_booking = await crud.delete_booking(db, booking_id=booking_id)
    return db_booking
