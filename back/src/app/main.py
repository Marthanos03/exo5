from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from src.app.router.booking_router import router
from src.app import models
from src.app.exceptions import BookingNotFoundException

DATABASE_URL_SYNC = "postgresql+psycopg2://postgres:password@db:5432/flight_booking_db"


def init_db():
    """init database"""
    engine = create_engine(DATABASE_URL_SYNC)
    models.Base.metadata.create_all(bind=engine)


app = FastAPI(on_startup=[init_db])
app.include_router(router)


@app.exception_handler(BookingNotFoundException)
def booking_not_found_exception_handler(request: Request, exc: BookingNotFoundException):
    """returns a 404 error"""
    return JSONResponse(
        status_code=404,
        content={"detail": f"Booking with ID {exc.booking_id} not found."},
    )
