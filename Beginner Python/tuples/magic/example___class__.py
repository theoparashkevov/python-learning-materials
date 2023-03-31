my_tuple = (1, 2, 3)

# Get the class object of my_tuple
tuple_class = my_tuple.__class__

# Create a new tuple instance using the class object
new_tuple = tuple_class([4, 5, 6])

print(new_tuple)  # Output: (4, 5, 6)
