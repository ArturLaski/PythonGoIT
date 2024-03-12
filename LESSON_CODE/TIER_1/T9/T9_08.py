def positive_values(list_payment):
    return list(filter(lambda x: x > 0, list_payment))

# Test the function
payment = [100, -3, 400, 35, -100]
print(positive_values(payment))
