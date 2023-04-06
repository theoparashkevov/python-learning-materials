class MyList:
    def __init__(self, elements):
        self.elements = elements

    def __lt__(self, other):
        return sum(self.elements) < sum(other.elements)

my_list1 = MyList([1, 2, 3])
my_list2 = MyList([4, 5, 6])
print(my_list1 < my_list2)  # prints True
