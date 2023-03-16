# Create a set
original_set = {1, 2, 3, 4}

# Use the copy function to create a new set with the same elements
copied_set = original_set.copy()

# Add an element to the original set
original_set.add(5)

# Print both sets to show that they are different
print("Original set:", original_set)  # Output: Original set: {1, 2, 3, 4, 5}
print("Copied set:", copied_set)      # Output: Copied set: {1, 2, 3, 4}
