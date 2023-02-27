from copy import deepcopy

example_list = [1, 2, 3, 'a', 'b', 'c', 'X', 'Y', 'Z']

# You can append any type of object to a list
# Integer
example_list.append(50)
print(example_list, '\n')

# Float
example_list.append(1.56)
print(example_list, '\n')

# String
example_list.append('String')
print(example_list, '\n')

# The same list
# Here we will get a pointer recursion i.e. the address of the list will contain an element pointing to the list itself
example_list.append(example_list)
print(example_list)
print('The id of the original list: ', id(example_list))
print('The id of the appended list: ', id(example_list[12]))
print('original list id ?= appended list id: ', id(example_list) == id(example_list[12]), '\n')

# A copy of the list
# Here we will not get a pointer recursion, because we are making a deep copy of the list and then appending the copy
example_list.append(deepcopy(example_list))
print(example_list)
print('The id of the original list: ', id(example_list))
print('The id of the appended list: ', id(example_list[13]))
print('original list id ?= appended list id: ', id(example_list) == id(example_list[13]), '\n')
