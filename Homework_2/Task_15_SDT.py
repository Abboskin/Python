string = input("Enter a string: ")
print("".join([string[i] for i in range(1, len(string), 2)]))
