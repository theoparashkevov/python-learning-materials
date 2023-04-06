class MyList(list):
    def __add__(self, other):
        return MyList(super().__add__(other))

# Create two instances of MyList
list1 = MyList([1, 2, 3])
list2 = MyList([4, 5, 6])

# Use the "+" operator to concatenate the two lists
result = list1 + list2

# Print the result
print(result)  # [1, 2, 3, 4, 5, 6]
print(type(result))  # <class '__main__.MyList'>
