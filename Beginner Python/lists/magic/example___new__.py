class CustomList(list):
	def __new__(cls, *args, **kwargs):
		# Create a new instance of CustomList
		instance = super().__new__(cls, *args, **kwargs)

		# Add a custom attribute to the instance
		instance.custom_attr = 0

		# Return the new instance
		return instance


custom_list = CustomList([1, 2, 3])
print(custom_list)  # Output: [1, 2, 3]
print(custom_list.custom_attr)  # Output: 0
