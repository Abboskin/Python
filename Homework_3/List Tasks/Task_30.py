my_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
is_sorted = my_list == sorted(my_list)
print("Is the list sorted in ascending order?", is_sorted)
