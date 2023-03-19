"""
The Liskov substitution principle states that any instance of a base class should be replaceable with an instance
of any of its derived classes without altering the correctness of the program. This principle ensures that the behavior
of a program remains consistent even if a different implementation of a class is used.

In this example, Shape is the base class and Rectangle and Square are its derived classes. Both Rectangle and Square
implement the area() method, but Square overrides the implementation of area() from Rectangle to return
the area of a square.

The print_area() function takes an instance of Shape as a parameter and calls its area() method to calculate its area.
Since Square is a subclass of Rectangle, it can be passed as an argument to the
print_area() function without any issues.

Thus, the Liskov substitution principle is upheld, and the program behaves correctly regardless of whether a Rectangle
or a Square object is passed to the print_area() function.
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


class Square(Rectangle):
	def __init__(self, side_length):
		super().__init__(side_length, side_length)

	def area(self):
		return super().area()


def print_area(shape):
	print(shape.area())


# create a rectangle object and calculate its area
r = Rectangle(2, 3)
print_area(r)  # Output: 6

# create a square object and calculate its area
s = Square(2)
print_area(s)  # Output: 4
