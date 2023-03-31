
class MyTuple(tuple):

    def __getitem__(self, index):
        return 'from __getitem__\t\t' + str(super().__getitem__(index))


my_tuple = MyTuple( [1, 2, 3, 4, 5] )

print(my_tuple[0])   # from __getitem__ 1
print(my_tuple[-1])  # from __getitem__ 5
print(my_tuple[2:4]) # from __getitem__ (3, 4)
