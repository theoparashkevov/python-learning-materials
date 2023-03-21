"""
The Common Closure Component Cohesion principle states that components should contain classes that have related
functionality and operate on related data. In Python, this can be achieved by creating classes that are focused
on a specific task or set of tasks that are related to each other.

In this example, we have three classes: Employee, Payroll, and Performance.
The Employee class represents the employees of a company and their basic information.
The Payroll class handles the calculation of the company's payroll based on the list of employees, while
the Performance class handles the calculation of the performance ratings of each employee.

By separating these functionalities into different classes, we achieve a higher level of cohesion within each class,
and we can easily make changes or additions to each class without affecting the other classes. Additionally,
the classes are related to each other, as they all deal with the employees of the company, which aligns with
the Common Closure Component Cohesion principle.
"""

class Employee:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_department(self):
        return self.department


class Payroll:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def remove_employee(self, employee):
        self.employee_list.remove(employee)

    def calculate_payroll(self):
        total_payroll = 0
        for employee in self.employee_list:
            total_payroll += employee.get_salary()
        return total_payroll


class Performance:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def remove_employee(self, employee):
        self.employee_list.remove(employee)

    def calculate_performance(self):
        performance_ratings = {}
        for employee in self.employee_list:
            performance_ratings[employee.get_name()] = employee.get_rating()
        return performance_ratings
