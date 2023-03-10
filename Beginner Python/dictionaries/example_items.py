example_dictionary = {1: 'str_1', 2: 'str_2', 3: 'str_3', '3': 3, '4': 4, '5': 5}
print(example_dictionary)

# item[0] => key
# item[1] => value
for item in example_dictionary.items():
    print(item, type(item), sep='\t\t')
