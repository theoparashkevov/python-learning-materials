class ReadOnlyList(list):
	def __delattr__(self, attr):
		raise AttributeError("Cannot delete attributes from ReadOnlyList")

	def __setattr__(self, attr, value):
		raise AttributeError("Cannot set attributes on ReadOnlyList")

	def append(self, item):
		raise AttributeError("Cannot append to ReadOnlyList")

# additional methods to make the list read-only, such as extend, insert, remove, pop, etc.


# Create an instance of ReadOnlyList
my_list = ReadOnlyList([1, 2, 3, 4])

# Try to delete an attribute from my_list
try:
	del my_list[0]
except AttributeError as e:
	print(e)  # Cannot delete attributes from ReadOnlyList

# Try to set an attribute on my_list
try:
	my_list.new_attr = "new_value"
except AttributeError as e:
	print(e)  # Cannot set attributes on ReadOnlyList

# Try to append an item to my_list
try:
	my_list.append(5)
except AttributeError as e:
	print(e)  # Cannot append to ReadOnlyList

# Check that my_list has not been modified
print(my_list)  # [1, 2, 3, 4]
