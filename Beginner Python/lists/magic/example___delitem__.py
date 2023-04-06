class NoNegativeIndexList(list):
    def __delitem__(self, index):
        if index < 0:
            raise IndexError("Negative indexing is not allowed")
        super().__delitem__(index)

# Create an instance of NoNegativeIndexList
my_list = NoNegativeIndexList([1, 2, 3, 4])

# Try to delete an item at index 1
del my_list[1]
print(my_list)  # [1, 3, 4]

# Try to delete an item at index -1 (should raise an error)
try:
    del my_list[-1]
except IndexError as e:
    print(e)  # Negative indexing is not allowed

# Check that my_list has not been modified
print(my_list)  # [1, 3, 4]
