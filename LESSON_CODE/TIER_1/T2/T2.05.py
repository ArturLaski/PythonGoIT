import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"The equation has two real roots: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x1 = x2 = -b / (2 * a)
    print(f"The equation has one real root: x1 = x2 = {x1}")
else:
    real_part = -b / (2 * a)
    imag_part = math.sqrt(abs(D)) / (2 * a)
    print(f"The equation has complex roots: x1 = {real_part} + {imag_part}i, x2 = {real_part} - {imag_part}i")
