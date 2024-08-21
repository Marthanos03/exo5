import datetime


def check_date(date: datetime) -> bool:
    "check if the date is after the actual date"
    if date < datetime.datetime.now + datetime.timedelta(hours=1):
        return False
    return True
