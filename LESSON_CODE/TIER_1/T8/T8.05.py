from decimal import Decimal, getcontext

def decimal_average(number_list, signs_count):
    # Convert all numbers in the list to Decimal type
    number_list = [Decimal(str(num)) for num in number_list]
    
    # Set precision for Decimal operations
    getcontext().prec = signs_count
    
    # Calculate sum of numbers
    total = sum(number_list)
    
    # Calculate the arithmetic mean
    average = total / len(number_list)
    
    return average

# Example usage:
result1 = decimal_average([3, 5, 77, 23, 0.57], 6)
print("Result 1:", result1)

result2 = decimal_average([31, 55, 177, 2300, 1.57], 9)
print("Result 2:", result2)