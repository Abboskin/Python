list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))
merged_sorted_list = sorted(list1 + list2)
print("Merged and sorted list:", merged_sorted_list)
