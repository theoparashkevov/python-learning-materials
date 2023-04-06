class MyList(list):
    def __eq__(self, other):
        if isinstance(other, MyList):
            return self.sort() == other.sort()
        return False

my_list1 = MyList([1, 2, 3])
my_list2 = MyList([3, 2, 1])
my_list3 = [1, 2, 3]

# Compare my_list1 and my_list2
print(my_list1 == my_list2)  # True

# Compare my_list1 and my_list3
print(my_list1 == my_list3)  # True
