number = int(input("Enter a positive integer: "))

for a in range(1, number + 1):
    if number % a == 0: 
        print(f"{a} is a factor of {number}")
