class MyTuple(tuple):
    def __eq__(self, other):
        if isinstance(other, MyTuple):
            return sorted(self) == sorted(other)
        return NotImplemented

my_tuple1 = MyTuple((1, 2, 3))
my_tuple2 = MyTuple((3, 2, 1))
my_tuple3 = (1, 2, 3)

print(my_tuple1 == my_tuple2)  # True
print(my_tuple1 == my_tuple3)  # True
print(my_tuple2 == my_tuple3)  # True
