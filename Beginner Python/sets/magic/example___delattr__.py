# Define a set
my_set = {1, 2, 3}

# Delete the "discard" method from the set
delattr(my_set, "discard")

# This will raise an AttributeError since the "discard" method no longer exists
my_set.discard(1)
