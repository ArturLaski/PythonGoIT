from datetime import datetime

def get_str_date(date):
    try:
        # Try parsing the input date string with time information
        parsed_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    except ValueError:
        # If parsing fails, try parsing the input date string without time information
        parsed_date = datetime.strptime(date, '%Y-%m-%d')

    # Format the datetime object into the desired string format
    formatted_date = parsed_date.strftime('%A %d %B %Y')

    return formatted_date