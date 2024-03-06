def add_employee_to_file(record, path):
    try:
        # Otwieramy plik w trybie do odczytu i zapisu
        file = open(path, "a")

        # Dodajemy nowego pracownika do pliku na końcu
        file.write(record + "\n")

        # Zamykamy plik
        file.close()
        print("Pomyślnie dodano pracownika do pliku.")
    except Exception as e:
        print("Wystąpił błąd podczas dodawania pracownika do pliku:", e)

# Ścieżka do pliku
path = "employees.txt"

# Nowy pracownik do dodania
new_employee = "Drake Mikelsson,19"

# Wywołanie funkcji dodawania pracownika do pliku
add_employee_to_file(new_employee, path)