my_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
start = int(input("Enter the start index of the sublist: "))
end = int(input("Enter the end index of the sublist: "))
sublist = my_list[start:end+1]
min_element = min(sublist)
print("Minimum of sublist:", min_element)
