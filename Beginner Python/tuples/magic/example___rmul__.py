class MyTuple(tuple):
    def __rmul__(self, other):
        return self * other


tup = MyTuple((1, 2, 3))
result = 3 * tup
print(result) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
