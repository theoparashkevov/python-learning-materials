class MySet:
	def __init__(self, values):
		self.values = set(values)

	def __eq__(self, other):
		return self.values == other.values


set1 = MySet([1, 2, 3])
set2 = MySet([2, 3, 1])
set3 = MySet([1, 2, 3, 4])

print(set1 == set2)  # True
print(set1 == set3)  # False
