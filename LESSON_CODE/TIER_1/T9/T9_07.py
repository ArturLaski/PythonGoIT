def get_emails(list_contacts):
    return list(map(lambda contact: contact["email"], list_contacts))

# Test the function
list_contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    }
]

print(get_emails(list_contacts))
