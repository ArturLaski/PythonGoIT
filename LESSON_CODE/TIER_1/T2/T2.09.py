num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    if sum != 0:
        num = int(input("Enter integer (0 for output): "))
    
    current_sum = 0
    for i in range(num+1):
        current_sum += i

    sum += current_sum
        
print(f"The sum of all entered numbers is: {sum}")
