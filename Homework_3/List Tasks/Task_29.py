my_list = input("Enter a list of elements separated by spaces: ").split()
index = int(input("Enter the index to remove: "))
if 0 <= index < len(my_list):
    my_list.pop(index)
print("List after removal:", my_list)