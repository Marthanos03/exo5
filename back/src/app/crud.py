from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.app import models, schemas
from src.app import exceptions
from src.app.utils import check_date, get_password_hash, verify_password


async def get_booking(db: AsyncSession, booking_id: int) -> schemas.Booking:
    """get a booking with an ID"""
    query = await db.execute(select(models.Booking).filter(models.Booking.id == booking_id))
    booking = query.scalar_one_or_none()
    if not booking:
        raise exceptions.BookingNotFoundException(booking_id)
    return booking


async def get_bookings(db: AsyncSession):
    """get all bookings"""
    bookings = await db.execute(select(models.Booking))
    return bookings.scalars().all()


async def create_booking(db: AsyncSession, booking: schemas.BookingCreate):
    """create a new booking"""
    if not check_date(booking.date):
        raise exceptions.BookingImpossibleDateException(-1)
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    await db.commit()
    await db.refresh(db_booking)
    return db_booking


async def update_booking(db: AsyncSession, booking_id: int, booking: schemas.BookingUpdate):
    """update a booking with an ID"""
    if not check_date(booking.date):
        raise exceptions.BookingImpossibleDateException(booking_id)
    db_booking = await get_booking(db, booking_id)
    for key, value in booking.dict().items():
        setattr(db_booking, key, value)
    await db.commit()
    await db.refresh(db_booking)
    return db_booking


async def patch_booking(db: AsyncSession, booking_id: int, booking: schemas.BookingPatch):
    """patch a booking with an ID"""
    if not check_date(booking.date):
        raise exceptions.BookingImpossibleDateException(booking_id)
    db_booking = await get_booking(db, booking_id)
    for key, value in booking.dict(exclude_unset=True).items():
        setattr(db_booking, key, value)
    await db.commit()
    await db.refresh(db_booking)
    return db_booking


async def delete_booking(db: AsyncSession, booking_id: int):
    """delete a booking with an ID"""
    db_booking = await get_booking(db, booking_id)
    await db.delete(db_booking)
    await db.commit()
    return db_booking

async def signup(db: AsyncSession, user: schemas.UserCreate):
    query = await db.execute(select(models.User).filter(models.User.username == user.username))
    db_user = query.scalar_one_or_none()
    if db_user:
        raise exceptions.UserAlreadyExistException(user.username)
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return user.username


async def login(db: AsyncSession, user: schemas.UserCreate,):
    query = await db.execute(select(models.User).filter(models.User.username == user.username))
    db_user = query.scalar_one_or_none()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise exceptions.InvalidCredentialsException(user.username)
    return user.username