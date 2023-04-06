class MyList(list):
    def __ge__(self, other):
        return len(self) >= len(other)

list1 = MyList([1, 2, 3])
list2 = MyList([4, 5])

print(list1 >= list2)  # True
print(list2 >= list1)  # False
