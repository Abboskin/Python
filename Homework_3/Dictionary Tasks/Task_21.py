sample_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_by_value = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print(sorted_by_value)
