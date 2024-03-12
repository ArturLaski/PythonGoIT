def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description
    else:
        return None


# Przykłady użycia

grade_function = get_student_grade("grade")
description_function = get_student_grade("description")

print(grade_function("A"))  # Output: 5
print(description_function("B"))  # Output: Very good

invalid_function = get_student_grade("invalid")
print(invalid_function)  # Output: None
