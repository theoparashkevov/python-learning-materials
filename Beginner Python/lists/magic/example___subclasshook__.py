class MyList(list):
    def __subclasshook__(cls, subclass):
        return (issubclass(subclass, list) or
                hasattr(subclass, '__getitem__') and
                hasattr(subclass, '__len__') and
                hasattr(subclass, '__iter__') and
                hasattr(subclass, 'append'))

# checking if a class is a subclass of MyList
class MySubList(MyList):
    pass

print(issubclass(list, MyList))  # False
print(issubclass(MyList, list))  # True
print(issubclass(MySubList, MyList))  # True
print(issubclass(tuple, MyList))  # False
print(issubclass(str, MyList))  # False
print(issubclass(set, MyList))  # False
