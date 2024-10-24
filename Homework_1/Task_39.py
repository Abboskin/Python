A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
D = B**2 - 4*A*C
x1 = (-B + D) / (2 * A)
x2 = (-B - D) / (2 * A)
print(f"Two solutions: x1 = {x1}, x2 = {x2}")

#to check A*x**2 + B*x + C = 0