my_list = input("Enter a list of elements separated by spaces: ").split()
repeat_count = int(input("Enter the number of times to repeat each element: "))
repeated_list = [element for element in my_list for _ in range(repeat_count)]
print("List with elements repeated:", repeated_list)
