def get_cats_info(path):
    cats_info = []  # Inicjalizujemy pustą listę słowników

    try:
        with open(path, "r") as file:
            # Iterujemy po każdej linii w pliku
            for line in file:
                # Usuwamy znak nowej linii z końca każdej linii
                line = line.strip()
                # Dzielimy linię na trzy części: ID, imię i wiek kota
                cat_id, cat_name, cat_age = line.split(",")
                # Tworzymy słownik z danymi kota i dodajemy go do listy
                cat_info = {"id": cat_id, "name": cat_name, "age": cat_age}
                cats_info.append(cat_info)

        return cats_info
    except Exception as e:
        print("Wystąpił błąd podczas odczytu pliku:", e)
        return None

# Ścieżka do pliku
path = "cats.txt"

# Wywołanie funkcji odczytu informacji o kotach z pliku
cats_list = get_cats_info(path)

# Wyświetlenie listy słowników z informacjami o kotach
print(cats_list)