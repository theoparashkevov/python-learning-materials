example_dictionary = {1: 'str_1', 2: 'str_2', 3: 'str_3', '3': 3, '4': 4, '5': 5}
print(example_dictionary)

# if the key exists, no action
example_dictionary.setdefault(1, 'default_val_for_1')
print('Key exists: ', example_dictionary)

# if the key does not exist, insert key with the default value
example_dictionary.setdefault(77, 'default_val_for_1')
print('Key does not exist: ', example_dictionary)