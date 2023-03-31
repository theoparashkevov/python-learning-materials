class MyTuple:
    def __init__(self, *args):
        self.data = args

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


t = MyTuple(1, 2, 3)

for i in t:
    print(i)

# Output: 1 2 3
