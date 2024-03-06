grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted = []
    index = 1
    for student, grade in students.items():
        formatted.append(f"{index:4}|{student:<10}|{grade:^5}|{grades.get(grade, 'N/A'):^5}")
        index += 1
    return formatted

# Example usage:
students = {"Nick": "A", "Olga": "B", "Boris": "FX", "Anna": "C"}
for el in formatted_grades(students):
    print(el)