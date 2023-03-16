# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

# Use the isdisjoint() function to check if the sets have any common elements
if set1.isdisjoint(set2):
    print("The sets have no common elements")
else:
    print("The sets have common elements")
