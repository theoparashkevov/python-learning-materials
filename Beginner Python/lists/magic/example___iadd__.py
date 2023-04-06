class MyList:
    def __init__(self, items):
        self.items = items

    def __iadd__(self, other):
        if isinstance(other, MyList):
            self.items.extend(other.items)
        else:
            self.items.extend(other)
        return self

my_list1 = MyList([1, 2, 3])
my_list2 = MyList([4, 5, 6])

my_list1 += my_list2

print(my_list1.items)  # Output: [1, 2, 3, 4, 5, 6]
