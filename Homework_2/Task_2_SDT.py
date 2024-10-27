string = input("Enter a string: ")
vowels = "aeiouAEIOU"
print("".join([ch for ch in string if ch not in vowels]))
