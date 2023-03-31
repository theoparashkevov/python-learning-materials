class MyTuple(tuple):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.name = "My Tuple"


s = MyTuple([1, 2, 3])
print(s)
print(s.name)
