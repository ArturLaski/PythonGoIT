def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    return dict(zip(keys, values))

keys = ["name", "age", "city"]
values = ["Andr", None, "New York"]
result = make_request(keys, values)
print(result)  # Output: {'name': 'Andr', 'city': 'New York'}