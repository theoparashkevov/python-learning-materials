class MyList:
    def __init__(self, elements):
        print('Initializing elements')
        self.elements = elements

my_list = MyList([1, 2, 3, 4, 5])

print(my_list.elements) # Output: [1, 2, 3, 4, 5]
