example_list = [1, 2, 2, 3, 3, 3, 'a', 'b', 'c', 'X', 'Y', 'Z']
print(example_list, '\n')

print('Popping one item ...')
popped_item_1 = example_list.pop()
print('Popped item: ', popped_item_1)
print(example_list, '\n')

print('Popping one item at index [2] ...')
popped_item_2 = example_list.pop(2)
print('Popped item: ', popped_item_2)
print(example_list, '\n')