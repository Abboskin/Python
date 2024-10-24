V1 = float(input("First car (km/h): "))
V2 = float(input("Second car (km/h): "))
S = float(input("Distance between them (km): "))
T = float(input("Time they travel (hours): "))

distance = S + (V1 + V2) * T
print(f"Distance between the cars after {T} hours: {distance} km")
