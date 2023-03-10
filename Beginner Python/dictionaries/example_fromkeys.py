example_dictionary = {1: 'str_1', 2: 'str_2', 3: 'str_3', '3': 3, '4': 4, '5': 5}
print(example_dictionary)

example_keys    = [1, 2, 3, '3', '4', '5']
default_value_for_all_keys = 0

example_values  = ['str_1', 'str_2', 'str_3', 3, 4, 5]

new_dictionary_from_keys = dict.fromkeys(example_keys, default_value_for_all_keys)
print('Dictionary from .fromkeys() ', new_dictionary_from_keys)

new_dictionary_from_zip = dict(zip(example_keys, example_values))
print('Dictionary from zip() ', new_dictionary_from_zip)