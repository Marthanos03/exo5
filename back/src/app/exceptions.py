class BookingNotFoundException(Exception):
    """class to handle exceptions"""
    def __init__(self, booking_id: int):
        self.booking_id = booking_id


class BookingImpossibleDateException(Exception):
    """if the date is already passed"""
    def __init__(self, booking_id: int):
        self.booking_id = booking_id
