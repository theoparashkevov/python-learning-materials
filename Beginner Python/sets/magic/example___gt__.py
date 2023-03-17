set1 = {1, 2, 3}
set2 = {2, 3}

# Using the > operator
print(set1 > set2)  # Output: True

# Using the __gt__ function
print(set1.__gt__(set2))  # Output: True
