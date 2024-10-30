sample_list = [1, 2, 3, 4, 5]
middle = len(sample_list) // 2
if len(sample_list) % 2 == 0:
    print("Middle Element:", sample_list[middle-1:middle+1])
else:
    print("Middle Element:", sample_list[middle])
