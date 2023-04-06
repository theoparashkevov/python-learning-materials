class MyList:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        print('Len')
        return len(self.elements)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # prints 5
