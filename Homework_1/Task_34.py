X = float(input("Chocolate weigh?: "))
A = float(input("How much does it cost?: "))
Y = float(input("How much konfet?: "))
B = float(input("How much do they cost?: "))

kg_chocolate = A/X
kg_konfet = B/Y

diff = abs(kg_chocolate - kg_konfet)
print(f"Difference in price is {diff}")


