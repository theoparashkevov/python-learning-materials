class MyTuple(tuple):
    def __getattribute__(self, name):
        if name.isdigit():
            index = int(name)
            if index < 0 or index >= len(self):
                raise IndexError("tuple index out of range")
            return self[index]
        else:
            return super().__getattribute__(name)

tuple1 = MyTuple((1, 2, 3, 4, 5))

print(tuple1[0])    # 1
print(tuple1[-1])   # 5
try:
    print(tuple1[5])    # IndexError: tuple index out of range
except IndexError as e:
    print(e)
print(tuple1.count(2))  # 1
print(tuple1.index(4))  # 3
