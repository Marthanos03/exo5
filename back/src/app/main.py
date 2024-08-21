from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from src.app.router.booking_router import router
from src.app import models, schemas, crud
from src.app import exceptions
from src.app.database import get_db


DATABASE_URL_SYNC = "postgresql+psycopg2://postgres:password@db:5432/flight_booking_db"


def init_db():
    """init database"""
    engine = create_engine(DATABASE_URL_SYNC)
    models.Base.metadata.create_all(bind=engine)


app = FastAPI(on_startup=[init_db])
app.include_router(router)

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/signup/", response_model=str)
async def signup(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    """endpoint to sigunp"""
    res = await crud.signup(db, user)
    return res


@app.post("/login/", response_model=str)
async def login(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    """endpoint to login"""
    res = await crud.login(db, user)
    return res


@app.exception_handler(exceptions.BookingNotFoundException)
def booking_not_found_exception_handler(request: Request, exc: exceptions.BookingNotFoundException):
    """returns a 404 error"""
    return JSONResponse(
        status_code=404,
        content={"detail": f"Booking with ID {exc.booking_id} not found."},
    )


@app.exception_handler(exceptions.BookingImpossibleDateException)
def booking_impossible_date_exception_handler(request: Request, exc: exceptions.BookingImpossibleDateException):
    """returns a 404 error"""
    return JSONResponse(
        status_code=404,
        content={"detail": f"Booking with ID {exc.booking_id} has a date that is already passed."},
    )


@app.exception_handler(exceptions.InvalidCredentialsException)
def invalid_credentials_handler(request: Request, exc: exceptions.InvalidCredentialsException):
    """returns a 404 error"""
    return JSONResponse(
        status_code=404,
        content={"detail": f"Username {exc.username} or password is invalid."},
    )


@app.exception_handler(exceptions.UserAlreadyExistException)
def user_already_exist_exception_handler(request: Request, exc: exceptions.UserAlreadyExistException):
    """returns a 404 error"""
    return JSONResponse(
        status_code=404,
        content={"detail": f"Username {exc.username} is already taken."},
    )