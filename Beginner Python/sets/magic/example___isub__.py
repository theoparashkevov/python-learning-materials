# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Subtract set2 from set1 using the __isub__ function
set1.__isub__(set2)

# Alternatively, you can use the -= operator to achieve the same result:
# set1 -= set2

# Print the updated set1
print(set1)
