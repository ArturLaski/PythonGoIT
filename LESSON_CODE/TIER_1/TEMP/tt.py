import pickle

class Record:
    def __init__(self, name, phone, address, email, birthday=None):
        self.name = name
        self.phone = self._validate_phone(phone)
        self.address = address
        self.email = email
        self.birthday = birthday

    def _validate_phone(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number. Please provide a 10-digit number.")
        return phone
    
    def _validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address.")
        return email    

    def add_birthday(self, date_str):
        self.birthday = Birthday(date_str)

def main():
    filename = 'address_book_data.dat'
    
    # Ręczne sprawdzenie danych w pliku
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            print("Dane w pliku:")
            print(data)
    except FileNotFoundError:
        print("Plik nie istnieje lub nie można go otworzyć.")

    # Wczytanie danych z pliku za pomocą pickle.load()
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            print("\nDane wczytane z pliku za pomocą pickle.load():")
            print(data)
    except FileNotFoundError:
        print("Plik nie istnieje lub nie można go otworzyć.")
    except Exception as e:
        print("Wystąpił błąd podczas wczytywania danych z pliku:", e)

if __name__ == "__main__":
    main()