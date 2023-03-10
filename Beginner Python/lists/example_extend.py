example_list = [1, 2, 2, 3, 3, 3, 'a', 'b', 'c', 'X', 'Y', 'Z']
print(example_list)

example_list.extend([11, 22, 33])
print(example_list)

# Will extend using first the values and the keys of the dictionary
example_list.extend({1: '11', 2: '22', 3: '33'})
print(example_list)

