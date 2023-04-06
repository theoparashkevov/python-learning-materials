class MyList:
    def __init__(self, items):
        self.items = tuple(items)

    def __hash__(self):
        return hash(self.items)

    def __eq__(self, other):
        return self.items == other.items

my_list1 = MyList([1, 2, 3])
my_list2 = MyList([1, 2, 3])

print(hash(my_list1))  # Output: 529344067295497451
print(hash(my_list2))  # Output: 529344067295497451
print(my_list1 == my_list2)  # Output: True
