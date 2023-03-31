class MyTuple:
    def __init__(self, data):
        self.data = tuple(data)

    def __len__(self):
        return len(self.data)


my_tuple = MyTuple([1, 2, 3, 4, 5])
print(len(my_tuple))  # Output: 5
