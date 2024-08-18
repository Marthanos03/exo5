class BookingNotFoundException(Exception):
    def __init__(self, booking_id: int):
        self.booking_id = booking_id
