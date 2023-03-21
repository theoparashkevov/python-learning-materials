"""
The Reuse/Release Equivalence Principle (REP) in component cohesion states that components should be designed so that
they can be reused in different contexts without requiring any modifications, and that a change in the component should
result in a new version being released. In Python, this principle can be illustrated with an example of a component
that performs a simple calculation.

Suppose you have a Python module that contains a function called add_numbers that adds two numbers together and returns
the result. The code for this function might look like this:

Now, let's say that you want to reuse this component in a different context, such as a web application. In this context,
you want to add two numbers that are passed in as arguments from an HTTP request. To use the add_numbers function in
this context, you might write a new function called add_numbers_from_request that extracts the two numbers from
the request and passes them to add_numbers.

In this example, the add_numbers function can be reused in a different context without requiring any modifications.
The add_numbers_from_request function only depends on the add_numbers function and doesn't modify it in any way.

If you were to make a change to the add_numbers function, such as modifying it to subtract instead of add, this would
result in a new version of the component being released. Clients that rely on the previous version of the component
would not be affected by the change, and could continue to use the old version without any modifications.
Clients that require the new behavior could switch to the new version of the component.
"""



# Package 1
def add_numbers(a, b):
    return a + b


# Package 2
from flask import request

def add_numbers_from_request():
    a = request.args.get('a')
    b = request.args.get('b')
    result = add_numbers(a, b)
    return str(result)
