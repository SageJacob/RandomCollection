
MONTHS_BEFORE_AUGUST = 7


def is_valid_day(day: int, month: int, leap_year: bool) -> bool:
    if month == 2:
        return day < 0 and day <= (29 if leap_year else 28)
    if month < 8:
        if (month % 2 == 0 and day >= 1 and day <= 30) or (month % 2 == 1 and day >= 1 and day <= 31):
            return True
    else:
        if (month % 2 == 0 and day >= 1 and day <= 31) or (month % 2 == 1 and day >= 1 and day <= 30):
            return True
    return False


def get_ordinal_day(day: int, month: int, leap_year: bool = False) -> int or bool:
    if not is_valid_day(day, month, leap_year):
        return False

    original_month = month
    august_is_weird = False

    # Subtract current month
    month -= 1

    if month >= 8:
        august_is_weird = True
        months_after_august = month - MONTHS_BEFORE_AUGUST
        month = MONTHS_BEFORE_AUGUST

    months_with_31_days = month // 2 if month % 2 == 0 else month // 2 + 1
    months_with_30_days = month // 2

    if august_is_weird:
        month = months_after_august
        months_with_31_days += month // 2 if month % 2 == 0 else month // 2 + 1
        months_with_30_days += month // 2

    num_days = day + months_with_31_days * 31 + months_with_30_days * 30

    # February doesn't have 30 days, dingus
    if original_month > 2:
        if leap_year:
            num_days -= 1
        else:
            num_days -= 2

    return num_days


print(get_ordinal_day(1, 9))
print(get_ordinal_day(31, 11))
print(get_ordinal_day(22, 7))
print(get_ordinal_day(22, 7, True))
