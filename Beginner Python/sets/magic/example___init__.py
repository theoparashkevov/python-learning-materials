class MySet(set):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "My Set"

s = MySet([1, 2, 3])
print(s)
print(s.name)