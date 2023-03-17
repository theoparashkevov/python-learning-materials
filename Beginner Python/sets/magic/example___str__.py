class MySet(set):
    def __str__(self):
        return f"MySet({', '.join(str(x) for x in self)})"

s = MySet([1, 2, 3])
print(s)  # Output: MySet(1, 2, 3)
