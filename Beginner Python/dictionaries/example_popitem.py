example_dictionary = {1: 'str_1', 2: 'str_2', 3: 'str_3', '3': 3, '4': 4, '5': 5}
print(example_dictionary)


popped_item_1 = example_dictionary.popitem()
print('\nItem 1: ', popped_item_1)

print(example_dictionary)

popped_item_2 = example_dictionary.popitem()
print('\nItem 2: ', popped_item_2)

print(example_dictionary)