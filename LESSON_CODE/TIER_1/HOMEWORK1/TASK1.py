from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Prepare data structure to store birthdays for each day of the week
    birthdays_per_week = defaultdict(list)
    
    # Get the current date
    today = datetime.today().date()
    
    # Iterate through each user
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Calculate birthday for this year
        birthday_this_year = birthday.replace(year=today.year)
        
        # If birthday has passed this year, consider next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Calculate the difference between birthday and current date
        delta_days = (birthday_this_year - today).days
        
        # Determine the day of the week for the birthday
        birthday_weekday_n = birthday_this_year.strftime("%A")
        birthday_weekday = birthday_this_year.weekday()
        
        print(f'{birthday}, {today}, {birthday_this_year}, {delta_days}, {birthday_weekday}, {birthday_weekday_n}') 
        birthday_weekday = (birthday_weekday) % 7
        print(f'{birthday}, {today}, {birthday_this_year}, {delta_days}, {birthday_weekday}, {birthday_weekday_n}') 
        # If birthday falls on a weekend, move it to Monday
        if birthday_weekday >= 5:
            birthday_weekday_n = "Monday"
            #print(f'{birthday}, {today}, {birthday_this_year}, {delta_days}, {birthday_weekday}') 
        # Store the user's name under the appropriate day of the week
        if birthday_weekday < 7:
            birthdays_per_week[birthday_weekday_n].append(name)
        print(f'{birthday}, {today}, {birthday_this_year}, {delta_days}, {birthday_weekday}, {birthday_weekday_n}') 
    # Display the result
    for day, birthdays in birthdays_per_week.items():
        print(f"{day}: {', '.join(birthdays)}")

# Example usage:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 20)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
]

get_birthdays_per_week(users)
