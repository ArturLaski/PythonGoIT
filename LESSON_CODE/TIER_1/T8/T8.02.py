from datetime import date

def get_days_in_month(month, year):
    # Determine the number of days in the given month and year
    if month == 2:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29  # Leap year: February has 29 days
        else:
            return 28  # Non-leap year: February has 28 days
    elif month in [4, 6, 9, 11]:
        return 30  # April, June, September, November have 30 days
    else:
        return 31  # All other months have 31 days