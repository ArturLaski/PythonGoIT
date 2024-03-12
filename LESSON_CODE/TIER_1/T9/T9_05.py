def format_phone_number(func):
    def wrapper(phone):
        new_phone = func(phone)  # Call the original function to get the normalized phone number
        if len(new_phone) == 10:  # Short number, add prefix +38
            return "+38" + new_phone
        elif len(new_phone) == 12:  # Full international number, add only the + sign
            return "+" + new_phone
        else:
            return new_phone  # Return unchanged if not a recognized format
    return wrapper

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

# Example usage
phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for number in phone_numbers:
    print(sanitize_phone_number(number))
