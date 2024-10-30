my_list = list(map(int, input("Enter a list of negative numbers separated by spaces: ").split()))
negative_sum = sum(num for num in my_list if num < 0)
print("Sum of negative numbers:", negative_sum)

