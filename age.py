"""Calendar age using month-end-clamped monthly anniversaries."""
from calendar import monthrange
from datetime import date


def calendar_age(birth, given):
    if given < birth:
        raise ValueError("Given date must not precede date of birth")
    months = (given.year - birth.year) * 12 + given.month - birth.month

    def anniversary(count):
        year, month = divmod(birth.year * 12 + birth.month - 1 + count, 12)
        return date(year, month + 1, min(birth.day, monthrange(year, month + 1)[1]))

    if anniversary(months) > given:
        months -= 1
    years, months_left = divmod(months, 12)
    return years, months_left, (given - anniversary(months)).days
