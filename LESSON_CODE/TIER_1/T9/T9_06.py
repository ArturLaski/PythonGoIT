def normal_name(list_name):
    return list(map(lambda name: name.capitalize(), list_name))

# Test the function
name = ["dan", "jane", "steve", "mike"]
print(normal_name(name))
