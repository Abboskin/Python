my_list = input("Enter a list of elements separated by spaces: ").split()
is_palindrome = my_list == my_list[::-1]
print("Is the list a palindrome?", is_palindrome)