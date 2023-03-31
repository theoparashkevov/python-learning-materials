class MyTuple:
    def __init__(self, *args):
        self.data = args

    def __hash__(self):
        return hash(self.data)


t1 = MyTuple(1, 2, 3)
t2 = MyTuple(1, 2, 3)

print(hash(t1))  # 529344067295497451
print(hash(t2))  # 529344067295497451
