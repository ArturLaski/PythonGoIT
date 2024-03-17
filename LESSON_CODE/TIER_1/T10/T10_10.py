class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith("01"):
        raise IDException("Employee ID must start with '01'")
    id_list.append(employee_id)
    return id_list

# Example usage:
try:
    ids = []
    ids = add_id(ids, "01234")  # This should raise an IDException
except IDException as e:
    print("Error:", e)

ids = add_id(ids, "01001")  # This should add the ID successfully
print(ids)  # Output: ['01001']
   
        