class SortedTuple(tuple):
    def __new__(cls, iterable):
        # Sort the iterable and create a new tuple object
        sorted_iterable = sorted(iterable)
        new_tuple = super().__new__(cls, sorted_iterable)
        return new_tuple


t1 = SortedTuple((3, 1, 4, 1, 5, 9, 2, 6, 5))
print(t1)  # (1, 1, 2, 3, 4, 5, 5, 6, 9)

t2 = SortedTuple(["orange", "apple", "banana", "pear"])
print(t2)  # ('apple', 'banana', 'orange', 'pear')
