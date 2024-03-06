def read_employees_from_file(path):
    employees = []  # Inicjalizujemy pustą listę pracowników
    
    try:
        # Otwieramy plik do odczytu
        file = open(path, "r")

        # Iterujemy po każdej linii w pliku
        for line in file:
            # Usuwamy znak nowej linii z końca każdej linii i dodajemy do listy pracowników
            employees.append(line.strip())

        # Zamykamy plik
        file.close()
        return employees  # Zwracamy listę pracowników
    except Exception as e:
        print("Wystąpił błąd podczas odczytu pliku:", e)
        return None  # Jeśli wystąpił błąd, zwracamy None

# Ścieżka do pliku
path = "employees.txt"

# Wywołanie funkcji odczytu pracowników z pliku
employees_list = read_employees_from_file(path)

# Wyświetlenie listy pracowników
print(employees_list)