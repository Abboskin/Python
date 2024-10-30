my_list = input("Enter a list of elements separated by spaces: ").split()
element = input("Enter the element to find indices for: ")
indices = [index for index, value in enumerate(my_list) if value == element]
print(f"Indices of element '{element}':", indices)
