class MySet(set):
    def __getattribute__(self, attr):
        print(f"Getting attribute {attr}")
        return super().__getattribute__(attr)

my_set = MySet([1, 2, 3])
print(my_set.pop())
