from functools import reduce

def sum_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers, 0)

# Test the function
numbers = [3, 4, 6, 9, 34, 12]
print(sum_numbers(numbers))
