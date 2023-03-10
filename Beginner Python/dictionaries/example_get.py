example_dictionary = {1: 'str_1', 2: 'str_2', 3: 'str_3', '3': 3, '4': 4, '5': 5}
print(example_dictionary)

# Get value for specific key
val_1 = example_dictionary.get(1)
print('Value for key [1] ', val_1)

# Default value if key does not exist
val_6 = example_dictionary.get(6, 'str_6')
print('Value for key [6] ', val_6)