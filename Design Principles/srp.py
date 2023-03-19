"""
The Single Responsibility principle states that a class should have only one reason to change.
This means that a class should have only one responsibility or job to do, and any changes to that responsibility
should be limited to that class only.

In this example, Employee is responsible for storing the information about an employee, such as their name, title,
and salary. The get_salary() method is responsible for returning the employee's salary.

The Payroll class is responsible for calculating the payroll for a list of employees. It has a single responsibility of
calculating payroll and does not deal with any other aspect of the system.

Using this design, if there is a change in the way payroll is calculated or a new feature related to an employee's
salary is introduced, only the Payroll class needs to be modified, and the Employee class does not need to be changed.
Similarly, if there is a change in the way employee data is stored or retrieved, only the Employee class needs to be
modified, and the Payroll class does not need to be changed.

Thus, the Single Responsibility principle ensures that classes are focused on doing one thing only, and it makes the
system easier to maintain and change in the future.
"""


class Employee:
	def __init__(self, name, title, salary):
		self.name = name
		self.title = title
		self.salary = salary

	def get_salary(self):
		return self.salary


class Payroll:
	def calculate_payroll(self, employees):
		print("Calculating payroll")
		for employee in employees:
			print(f"Payroll for {employee.name} - {employee.get_salary()}")
