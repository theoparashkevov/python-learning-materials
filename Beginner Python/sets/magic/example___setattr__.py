class MySet(set):
    def __setattr__(self, attr, value):
        if attr == "size":
            raise AttributeError("Cannot set size attribute.")
        else:
            super().__setattr__(attr, value)


s = MySet([1, 2, 3])
s.add(4)
print(s)
setattr(s, 'size', 4) # Output: AttributeError("Cannot set size attribute.")
