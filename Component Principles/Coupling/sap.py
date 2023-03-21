"""

The Stable Abstractions Principle (SAP) in component coupling states that components should be designed with a stable
level of abstraction, meaning that the level of abstraction should remain constant over time. In Python,
this principle can be illustrated with an example of a program that consists of multiple modules.

Suppose you have a Python program that consists of three modules: module1, module2, and module3. module1 is a
high-level module that provides a user interface for the program, module2 is a mid-level module that provides
business logic, and module3 is a low-level module that provides database access. Each module has a different
level of abstraction, with module1 being the most abstract and module3 being the most concrete.

In this example, we can enforce the SAP by ensuring that the level of abstraction for each module remains constant
over time. This means that module1 should always remain a high-level module that provides a user interface,
while module2 should always remain a mid-level module that provides business logic, and module3 should always
remain a low-level module that provides database access.

To enforce the SAP in Python, you can follow a few best practices for module design:

Choose an appropriate level of abstraction for each module. Each module should have a specific and well-defined purpose,
and should be designed at an appropriate level of abstraction.

Minimize changes to the level of abstraction over time. Avoid making changes to a module that would cause its level
of abstraction to change significantly.

Use encapsulation to hide implementation details. By hiding implementation details, you can reduce the coupling between
modules and make it easier to change the implementation of a module without affecting the other modules
that depend on it.

In our example, we can follow these best practices by designing our modules to be encapsulated and maintain a stable
level of abstraction. For example, we might define interfaces for the database access in module3, so that
module2 can depend on the interfaces rather than the implementation details of module3.
This can make it easier to change the database implementation without affecting the rest of the program,
while still maintaining the same level of abstraction for each module. Similarly, we might use encapsulation
in module2 to hide the implementation details of the business logic, so that changes to the implementation
do not affect the level of abstraction for module1 or module3.

"""