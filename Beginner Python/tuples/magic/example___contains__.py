class MyTuple:
    def __init__(self, data):
        self.data = tuple(data)

    # Define a custom __contains__ method for MyTuple
    def __contains__(self, value):
        return value % 2 == 0


my_tuple = MyTuple([1, 2, 3, 4, 5])

# Check if values are present in my_tuple using the in operator
print(2 in my_tuple)  # Output: True
print(3 in my_tuple)  # Output: False
print(4 in my_tuple)  # Output: True
print(5 in my_tuple)  # Output: False
