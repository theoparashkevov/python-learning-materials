class MyTuple(tuple):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"A new subclass of MyTuple has been defined: {cls}")

# create a subclass of MyTuple
class MySubTuple(MyTuple):
    pass

# create another subclass of MyTuple
class MyOtherSubTuple(MyTuple):
    pass

# create an instance of MySubTuple
s = MySubTuple([1, 2, 3])

# create an instance of MyOtherSubTuple
t = MyOtherSubTuple([4, 5, 6])