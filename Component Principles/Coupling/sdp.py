"""

The Stable Dependencies Principle (SDP) in component coupling states that high-level components should be more stable
and have fewer dependencies than low-level components. In Python, this principle can be illustrated with an example
of a program that consists of multiple modules.

Suppose you have a Python program that consists of three modules: module1, module2, and module3. module1 is a
high-level module that provides a user interface for the program, module2 is a mid-level module that provides
business logic, and module3 is a low-level module that provides database access. module1 depends on module2,
module2 depends on module3, and module3 does not depend on any other module.

In this example, module1 is more stable than module2 and module3 because it has fewer dependencies and is less
likely to change. If module2 or module3 were to change, it would have a greater impact on the stability of
the program than if module1 were to change.

To enforce the SDP in Python, you can follow a few best practices for module design:

Group related functionality into cohesive modules. Modules should have a clear and specific purpose, and should not be
too large or too small.

Minimize dependencies between modules. Avoid unnecessary dependencies between modules, and try to keep high-level
modules from depending on low-level modules.

Use interfaces and abstraction to decouple modules. By defining interfaces and using abstraction, you can reduce
the coupling between modules and make it easier to change the implementation of a module without affecting the
other modules that depend on it.

In our example, we can follow these best practices by designing our modules to be cohesive and decoupled. For example,
we might define interfaces for the database access in module3, so that module2 can depend on the interfaces rather
than the implementation details of module3. This can make it easier to change the database implementation without
affecting the rest of the program. Similarly, we might use interfaces in module2 to decouple it from module1,
so that changes to the user interface do not require changes to the business logic.

"""