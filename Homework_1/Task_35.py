V = float(input("Boat in still water (km/h): "))
U = float(input("River(km/h): "))
S = float(input("Distance(km): "))

time_with_current = S / (V + U)
time_against_current = S / (V - U)
print(f"Time with current: {time_with_current} hours, Time against current: {time_against_current} hours")
