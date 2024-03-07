import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):
    if isinstance(cats[0], dict):  # If list contains dictionaries
        return [Cat(**cat) for cat in cats]
    elif isinstance(cats[0], Cat):  # If list contains named tuples
        return [cat._asdict() for cat in cats]

# Example usage:
# Mode 1: Convert list of named tuples to list of dictionaries
cats_named_tuples = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
result1 = convert_list(cats_named_tuples)
print("Result 1:", result1)

# Mode 2: Convert list of dictionaries to list of named tuples
cats_dicts = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
result2 = convert_list(cats_dicts)
print("Result 2:", result2)