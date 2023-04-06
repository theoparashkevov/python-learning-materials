class MyList(list):
    def __reversed__(self):
        return self[::-1]

my_list = MyList([1, 2, 3])
for i in reversed(my_list):
    print(i) # output: 3, 2, 1

