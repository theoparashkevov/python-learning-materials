example_list = [1, 2, 2, 3, 3, 3, 'a', 'b', 'c', 'X', 'Y', 'Z']
print(example_list, '\n')

try:
    example_list.insert('T')
except TypeError as e:
    print('[Error] The exception text is: ', e)
print(example_list, '\n')

# Insert an object at a specific position
example_list.insert(1, 'T_T')
print(example_list, '\n')