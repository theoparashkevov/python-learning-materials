class MyList:
    def __init__(self, items):
        self.items = items

    def __imul__(self, n):
        self.items *= n
        return self

my_list = MyList([1, 2, 3])

my_list *= 3

print(my_list.items)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
