class CustomSet(set):
    def __repr__(self):
        return f"CustomSet({super().__repr__()})"

# Create a new set
s = CustomSet([1, 2, 3])

# Call __repr__() on the set
print(repr(s))
