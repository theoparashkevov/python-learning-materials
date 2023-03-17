class MySet(set):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"A new subclass of MySet has been defined: {cls}")

# create a subclass of MySet
class MySubSet(MySet):
    pass

# create another subclass of MySet
class MyOtherSubSet(MySet):
    pass

# create an instance of MySubSet
s = MySubSet([1, 2, 3])

# create an instance of MyOtherSubSet
t = MyOtherSubSet([4, 5, 6])
