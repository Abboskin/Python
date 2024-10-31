def change_c_to_f(c):
    return c * 9 / 5 + 32

def change_f_to_c(f):
    return (f - 32) * 5 / 9

f = float(input("Enter a temperature in degrees F: "))
c = change_f_to_c(f)
print(f"{f} degrees F = {round(c, 2)} degrees C")

c = float(input("Enter a temperature in degrees C: "))
f = change_c_to_f(c)
print(f"{c} degrees C = {round(f, 2)} degrees F")
