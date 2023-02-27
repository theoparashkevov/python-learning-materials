example_list = [1, 2, 3, 'a', 'b', 'c', 'X', 'Y', 'Z']
print(example_list)

example_list_copy = example_list.copy()
print(example_list_copy)

print('The id of the original list: ', id(example_list))
print('The id of the copied   list: ', id(example_list_copy))
print('original list id ?= copied list id: ', id(example_list) == id(example_list_copy), '\n')