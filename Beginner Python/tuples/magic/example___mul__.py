class MyTuple:
    def __init__(self, *args):
        self.data = args

    def __mul__(self, n):
        return MyTuple(*(self.data * n))


t1 = MyTuple(1, 2, 3)
t2 = t1 * 3
t3 = t1 * 0

print(t2.data)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(t3.data)  # ()
