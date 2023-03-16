class MySet(set):
    def __class_getitem__(cls, item):
        return cls(range(item))

s = MySet[5] # creates a set containing {0, 1, 2, 3, 4}

print(s)