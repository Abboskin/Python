my_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
positive_sum = sum(num for num in my_list if num > 0)
print("Sum of positive numbers:", positive_sum)
