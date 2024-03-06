from datetime import datetime

def get_days_from_today(date):
    # Convert the input date string to a datetime object
    input_date = datetime.strptime(date, '%Y-%m-%d').date()

    # Get the current date
    current_date = datetime.now().date()

    # Calculate the difference in days between the current date and the input date
    difference = (current_date - input_date).days

    return difference