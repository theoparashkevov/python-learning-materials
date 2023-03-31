class MyTuple:
    def __init__(self, data):
        self.data = tuple(data)

    def __add__(self, other):
        if isinstance(other, MyTuple):
            return MyTuple(self.data + other.data)
        elif isinstance(other, tuple):
            return MyTuple(self.data + other)
        else:
            raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")


my_tuple1 = MyTuple([1, 2, 3])
my_tuple2 = MyTuple([4, 5, 6])
my_tuple3 = (7, 8, 9)

# Adding two MyTuple instances
my_tuple_sum1 = my_tuple1 + my_tuple2
print(my_tuple_sum1.data)  # Output: (1, 2, 3, 4, 5, 6)

# Adding a MyTuple instance and a tuple
my_tuple_sum2 = my_tuple1 + my_tuple3
print(my_tuple_sum2.data)  # Output: (1, 2, 3, 7, 8, 9)

# Trying to add unsupported types
my_tuple_sum3 = my_tuple1 + "abc"  # Raises TypeError
