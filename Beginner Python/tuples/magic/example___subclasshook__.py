class MyTuple(tuple):
    def __subclasshook__(cls, subclass):
        if cls is tuple:
            if issubclass(subclass, MyTuple):
                return True
        return NotImplemented


tup = MyTuple([1, 2, 3])
print(issubclass(MyTuple, tuple))  # True
