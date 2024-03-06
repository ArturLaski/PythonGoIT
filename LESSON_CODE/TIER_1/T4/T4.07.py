def is_valid_pin_codes(pin_codes):
    # Check if the list is empty
    if not pin_codes:
        return False
    
    # Check for duplicate pin codes
    if len(pin_codes) != len(set(pin_codes)):
        return False
    
    # Check if all pin codes are of length 4 and contain only digits
    for pin in pin_codes:
        if len(pin) != 4 or not pin.isdigit():
            return False
    
    return True