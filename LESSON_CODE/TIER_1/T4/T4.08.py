def is_valid_password(password):
    # Check if the length of the password is eight characters
    if len(password) != 8:
        return False
    
    # Check if it contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check if it contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check if it contains at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    return True