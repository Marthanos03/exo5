import datetime
from passlib.context import CryptContext


def check_date(date: datetime) -> bool:
    "check if the date is after the actual date"
    if date.timestamp() < (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).timestamp():
        return False
    return True


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
