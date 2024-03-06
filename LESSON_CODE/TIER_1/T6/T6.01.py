def write_employees_to_file(employee_list, path):
    try:
        # Otwieramy plik do zapisu
        file = open(path, "w")

        # Iterujemy po każdej liście pracowników dla każdego działu
        for department in employee_list:
            # Iterujemy po każdym pracowniku w danym dziale i zapisujemy do pliku
            for employee in department:
                file.write(employee + "\n")  # Zapisujemy pracownika na nowej linii

        # Zamykamy plik
        file.close()
        print("Zapisano dane do pliku:", path)
    except Exception as e:
        print("Wystąpił błąd podczas zapisu do pliku:", e)

# Przykładowe dane
employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

# Ścieżka do pliku
path = "employees.txt"

# Wywołanie funkcji zapisu do pliku
write_employees_to_file(employee_list, path)