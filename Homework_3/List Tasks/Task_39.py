my_list = input("Enter a list of elements separated by spaces: ").split()
size = int(input("Enter the number of elements per sublist: "))
nested_list = [my_list[i:i + size] for i in range(0, len(my_list), size)]
print("Nested list:", nested_list)
