"""
The Open-Closed principle states that software entities (classes, modules, functions) should be open for extension but
closed for modification. This means that you should be able to extend the behavior of a system without modifying
its existing codebase.

In this example, Shape is the base class, and Rectangle and Circle are its derived classes. Both classes implement the
area() method to calculate their respective areas.

The calculate_area() function takes a list of Shape objects as an argument and iterates over them to calculate the total
area of all shapes. Since Shape is open for extension, we can easily add new shapes to the system without modifying the
existing code. For example, we can add a new Triangle class that inherits from Shape and implements
its own area() method.

We can then create a Triangle object and add it to the shapes list without modifying the calculate_area() function.
"""


class Shape:
	def area(self):
		pass


class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height


class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 3.14 * self.radius ** 2


def calculate_area(shapes):
	total_area = 0
	for shape in shapes:
		total_area += shape.area()
	return total_area


# create a rectangle and a circle
r = Rectangle(2, 3)
c = Circle(5)

# calculate the total area of the shapes
shapes = [r, c]
total_area = calculate_area(shapes)

print(total_area)  # Output: 84.5


class Triangle(Shape):
	def __init__(self, base, height):
		self.base = base
		self.height = height

	def area(self):
		return 0.5 * self.base * self.height

t = Triangle(4, 2)
shapes.append(t)

total_area = calculate_area(shapes)
print(total_area)  # Output: 88.5
