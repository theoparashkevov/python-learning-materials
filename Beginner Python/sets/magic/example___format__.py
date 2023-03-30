# Define a custom class that inherits from set
class CustomSet(set):
    # Override the __format__ method to return a custom string representation
    def __format__(self, format_spec):

        # Format the set using the built-in str.format() method
        formatted_set = str(self).replace('{', '{{').replace('}', '}}')

        # Return the formatted string
        return formatted_set.__format__(format_spec)


# Create a CustomSet object
my_set = CustomSet([1, 2, 3])

# Use the format() function to format the set with a custom format string
formatted_set = format(my_set, '')
print('Formatted Set => ', formatted_set)

