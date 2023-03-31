from typing import TypeVar, Tuple

T = TypeVar('T')


class MyTuple(Tuple[T, T]):
    def __class_getitem__(cls, params):
        # Customize the creation of the MyTuple class with type hints
        # by adding a __name__ attribute to the class
        cls.__name__ = f'MyTuple[{params.__name__}]'
        return super().__class_getitem__(params)


# Create a new MyTuple class with type hints
MyIntTuple = MyTuple[int]

# Create a new MyIntTuple instance
my_int_tuple = MyIntTuple((1, 2))

print(my_int_tuple)  # Output: (1, 2)
print(type(my_int_tuple))  # Output: <class '__main__.MyTuple[int]'>
print(MyIntTuple.__name__)  # Output: MyTuple[int]
