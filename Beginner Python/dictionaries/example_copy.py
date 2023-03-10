example_dictionary = {1: 'str_1', 2: 'str_2', 3: 'str_3', '3': 3, '4': 4, '5': 5}
print(example_dictionary)

example_dictionary_copy = example_dictionary.copy()
print(example_dictionary_copy)

print('The id of the original dictionary: ', id(example_dictionary))
print('The id of the copied   dictionary: ', id(example_dictionary_copy))
print('original dictionary id ?= copied dictionary id: ', id(example_dictionary) == id(example_dictionary_copy), '\n')