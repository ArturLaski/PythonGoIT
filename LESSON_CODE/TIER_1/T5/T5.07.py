def formatted_numbers():
    formatted = []
    formatted.append(f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|")
    for num in range(16):
        hex_num = hex(num)[2:]
        binary_num = bin(num)[2:]
        formatted.append(f"|{num:<10}|{hex_num:^10}|{binary_num:>10}|")
    return formatted

# Example usage:
for el in formatted_numbers():
    print(el)