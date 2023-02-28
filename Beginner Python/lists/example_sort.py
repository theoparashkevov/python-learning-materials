example_list = [1, 2, 2, 3, 3, 3, 'a', 'b', 'c', 'X', 'Y', 'Z']
print(example_list, '\n')

try:
    example_list.sort()
except TypeError as e:
    print('[Error] The exception text is: ', e)
    example_list.remove('a')
    example_list.remove('b')
    example_list.remove('c')
    example_list.remove('X')
    example_list.remove('Y')
    example_list.remove('Z')

example_list.sort()
print(example_list)

example_list.sort(reverse=True)
print(example_list)