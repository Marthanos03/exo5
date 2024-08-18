from fastapi import FastAPI, Request
from src.app import models
from src.app.database import engine
from src.app.router.booking_router import router
from fastapi.responses import JSONResponse
from src.app.exceptions import BookingNotFoundException

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router)


@app.exception_handler(BookingNotFoundException)
def booking_not_found_exception_handler(request: Request, exc: BookingNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": f"Booking with ID {exc.booking_id} not found."},
    )
