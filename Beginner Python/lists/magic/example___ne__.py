class MyList:
    def __init__(self, elements):
        self.elements = elements

    def __ne__(self, other):
        if isinstance(other, MyList):
            return self.elements != other.elements
        else:
            return True

my_list1 = MyList([1, 2, 3])
my_list2 = MyList([1, 2, 4])
my_list3 = MyList([1, 2, 3])

print(my_list1 != my_list2)  # prints True
print(my_list1 != my_list3)  # prints False
print(my_list1 != [1, 2, 3])  # prints True
