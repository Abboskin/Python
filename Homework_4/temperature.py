def convert_cel_to_far(c):
    return c * 9 / 5 + 32
def convert_far_to_cel(f):
    return (f - 32) * 5 / 9
f = float(input("Enter a temperature in degrees F: "))
c = convert_far_to_cel(f)
print(f"{f} degrees F = {round(c, 2)} degrees C")
c = float(input("Enter a temperature in degrees C: "))
f = convert_cel_to_far(c)
print(f"{c} degrees C = {round(f, 2)} degrees F")
