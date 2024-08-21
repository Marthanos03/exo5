class BookingNotFoundException(Exception):
    """class to handle exceptions"""
    def __init__(self, booking_id: int):
        self.booking_id = booking_id


class BookingImpossibleDateException(Exception):
    """if the date is already passed"""
    def __init__(self, booking_id: int):
        self.booking_id = booking_id

class UserAlreadyExistException(Exception):
    """if the username already exist"""
    def __init__(self, username: str):
        self.username = username
        
class InvalidCredentialsException(Exception):
    """if the credentials are invalids"""
    def __init__(self, username: str):
        self.username = username