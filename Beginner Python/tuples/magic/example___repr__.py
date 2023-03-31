class MyTuple(tuple):
    def __repr__(self):
        return f'MyTuple({super().__repr__()})'


tup = MyTuple((1, 2, 3))
print(tup)
