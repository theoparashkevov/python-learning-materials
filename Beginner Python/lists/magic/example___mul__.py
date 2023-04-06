class MyList:
    def __init__(self, elements):
        self.elements = elements

    def __mul__(self, n):
        return self.elements * n

my_list = MyList([1, 2, 3])
print(my_list * 3)  # prints MyList([1, 2, 3, 1, 2, 3, 1, 2, 3])
