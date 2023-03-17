# Define two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Use the __ior__() function to compute the union of set1 and set2
set1.__ior__(set2)

# Print the result (set1 now contains the union of set1 and set2)
print(set1)
