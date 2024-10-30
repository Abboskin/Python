my_list = input("Enter a list of elements separated by spaces: ").split()
unique_list = []
[unique_list.append(item) for item in my_list if item not in unique_list]
print("List with unique elements in order:", unique_list)
