tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

print(tuple1 >= tuple2)  # False
print(tuple2 >= tuple1)  # True

class MyTuple(tuple):
    def __ge__(self, other):
        if len(self) != len(other):
            raise ValueError("Tuples must have same length to compare")
        for i in range(len(self)):
            if self[i] < other[i]:
                return False
            elif self[i] > other[i]:
                return True
        return True

tuple3 = MyTuple((1, 2, 3))
tuple4 = MyTuple((1, 2, 4))

print(tuple3 >= tuple4)  # False
print(tuple4 >= tuple3)  # True
