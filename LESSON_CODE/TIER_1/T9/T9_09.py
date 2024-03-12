def get_favorites(contacts):
    return list(filter(lambda contact: contact["favorite"], contacts))

# Test the function
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    },
    {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "phone": "(111) 222-3333",
        "favorite": True,
    }
]

print(get_favorites(contacts))
