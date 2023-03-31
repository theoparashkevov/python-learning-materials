# Define a tuple
my_tuple = (1, 2, 3)

# Delete the "count" method from the tuple
delattr(my_tuple, "count")

# This will raise an AttributeError since the "count" method no longer exists
my_tuple.count(1)
