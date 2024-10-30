my_list = input("Enter a list of elements separated by spaces: ").split()
shift = int(input("Enter the number of positions to rotate right: "))
rotated_list = my_list[-shift:] + my_list[:-shift]
print("Rotated list:", rotated_list)
