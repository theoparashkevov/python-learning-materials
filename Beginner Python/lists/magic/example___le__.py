class MyList:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        return len(self.elements)

    def __le__(self, other):
        return len(self) <= len(other)

list1 = MyList([1, 2, 3, 4, 5])
list2 = MyList([1, 2, 3])

print(list1 <= list2)  # prints False
print(list2 <= list1)  # prints True
