class MyList(list):
    def __gt__(self, other):
        print("Comparing lists")
        return super().__gt__(other)

list1 = MyList([1, 2, 3])
list2 = MyList([4, 5, 6])

if list1 > list2:
    print("List 1 is greater")
else:
    print("List 2 is greater")
