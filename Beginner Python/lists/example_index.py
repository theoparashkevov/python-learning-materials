example_list = [1, 2, 2, 3, 3, 3, 'a', 'b', 'c', 'X', 'Y', 'Z']
print(example_list)

index_of_1 = example_list.index(1)
print('Index of 1: ', index_of_1)

index_of_2 = example_list.index(2)
print('Index of 2: ', index_of_2)

index_of_2_start_1_end_len = example_list.index(2, 1, len(example_list))
print('Index of 2: ', index_of_2_start_1_end_len)

index_of_2_start_2_end_len = example_list.index(2, 2, len(example_list))
print('Index of 2: ', index_of_2_start_2_end_len)

try:
    index_of_2_start_3_end_len = example_list.index(2, 3, len(example_list))
except ValueError as e:
    print('[Error] The exception text is: ', e)
    print('Index of 2: start index passed the last occurrence of the number 2')