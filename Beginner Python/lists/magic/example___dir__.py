class MyList(list):
    def __dir__(self):
        return ['add', 'remove', 'get', 'set', 'length']

my_list = MyList([1, 2, 3])

# Get a list of attributes and methods of my_list
dir_list = dir(my_list)

# Print the list
print(dir_list)
