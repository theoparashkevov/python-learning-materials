class MyTuple(tuple):
    def __setattr__(self, name, value):
        raise AttributeError("Cannot set attribute in a tuple")


tup = MyTuple((1, 2, 3))
tup.foo = "bar"  # Raises an AttributeError
