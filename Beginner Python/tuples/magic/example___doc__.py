class MyTuple(tuple):
    """
    MyTuple is a custom tuple class that represents a collection of values.
    It provides several methods for working with the values, such as sorting and indexing.
    """

    def __new__(cls, values):
        return super().__new__(cls, values)

    def sorted(self):
        """
        sorted() returns a new MyTuple object with the values sorted in ascending order.
        """
        return MyTuple(sorted(self))

my_tuple = MyTuple((5, 3, 1, 4, 2))

# Print the documentation for the MyTuple class
print(MyTuple.__doc__)

# Print the documentation for the sorted() method
print(MyTuple.sorted.__doc__)

# Print the documentation for the my_tuple object
print(my_tuple.__doc__)
