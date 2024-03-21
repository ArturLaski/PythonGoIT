import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert favorite string to boolean
            row['favorite'] = row['favorite'].lower() == 'true'
            contacts.append(row)
    return contacts
