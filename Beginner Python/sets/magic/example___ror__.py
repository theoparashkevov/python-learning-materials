class MySet:
    def __init__(self, elements):
        self.elements = set(elements)

    def __ror__(self, other):
        return MySet(list(other) + list(self.elements))

s1 = MySet([1, 2, 3])
s2 = [4, 5]

result = s2 | s1
print(result.elements)  # Output: {1, 2, 3, 4, 5}
