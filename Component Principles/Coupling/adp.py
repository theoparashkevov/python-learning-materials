"""
The Acyclic Dependencies Principle (ADP) in component coupling states that the dependencies between components
should form a directed acyclic graph (DAG), meaning that there should be no circular dependencies between components.
In Python, this principle can be illustrated with an example of a program that consists of multiple modules.

Suppose you have a Python program that consists of three modules: module1, module2, and module3. module1 depends
on module2, module2 depends on module3, and module3 does not depend on any other module.
The dependencies between the modules can be represented by the following DAG:

module3
   |
module2
   |
module1


This is an example of a DAG because the dependencies between the modules form a directed graph that has no cycles.

If there were a circular dependency between the modules, such as module1 depending on module2, module2 depending
on module3, and module3 depending on module1, then the dependencies would form a cycle and violate the ADP.

In Python, the ADP can be enforced by following a few best practices for module imports:

Avoid circular imports between modules. If two modules depend on each other, consider refactoring the code
to remove the circular dependency.

Import only the symbols you need from other modules. Avoid importing entire modules when you only need a small
subset of their functionality. This can help reduce the likelihood of circular dependencies.

Use dependency injection to reduce coupling between modules. Instead of importing a module directly, pass an instance
of the module or a specific object from the module as an argument to the function or method that needs it.
This can help reduce coupling between modules and make it easier to test and maintain the code.
"""