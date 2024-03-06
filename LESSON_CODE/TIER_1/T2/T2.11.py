sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    
    current_sum = 0
    for i in range(num + 1):
        if i % 2 == 1:
            continue
        current_sum += i
    sum += current_sum
        
print(f"The sum of all entered numbers is: {sum}")