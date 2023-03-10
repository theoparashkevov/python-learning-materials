example_dictionary = {1: 'str_1', 2: 'str_2', 3: 'str_3', '3': 3, '4': 4, '5': 5}
print(example_dictionary)

for value in example_dictionary.values():
    print(value, type(value), sep='\t\t')