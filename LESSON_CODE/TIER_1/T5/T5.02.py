def sanitize_phone_number(phone):
    return (''.join(i for i in phone if i.isalnum()))  
        
        