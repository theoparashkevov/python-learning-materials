class MyTuple:
    def __init__(self, *args):
        self.data = args

    def __ne__(self, other):
        if not isinstance(other, MyTuple):
            return True
        return self.data != other.data


t1 = MyTuple(1, 2, 3)
t2 = MyTuple(1, 2, 3)
t3 = MyTuple(4, 5, 6)

print(t1 != t2)  # False
print(t1 != t3)  # True
print(t1 != "not a tuple")  # True
