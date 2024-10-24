x1 = float(input("First x: "))
y1 = float(input("First y: "))
x2 = float(input("Second x: "))
y2 = float(input("Second y: "))
x3 = float(input("Third x: "))
y3 = float(input("Third y: "))

a = abs(x1 - y1)
b = abs(x2 - y2)
c = abs(x3 - y3)

P = (a + b + c)*2
S = (P*(P-a)*(P-b)*(P-c))**0.5

print(f"Perimiter is:{P} and area is:{S}")
