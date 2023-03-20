"""
The Interface Segregation principle states that a class should not be forced to implement methods it does not use.
Instead, it should have multiple interfaces that are tailored to its specific needs.
This principle encourages the use of smaller, more specific interfaces to promote flexibility, reduce coupling,
and prevent unnecessary dependencies.

In this example, Document is a base class that represents a document with a title and content.
Instead of having a single interface with both print and save methods, we define two separate interfaces:
Printable and Savable.

We then create two separate classes PrintableDocument and SavableDocument which
implement the Printable and Savable interfaces, respectively.

The PrintableDocument class implements the print() method to print the document's title and content,
while the SavableDocument class implements the save() method to save the document's title and content.

Using this design, we can create different types of documents that implement only the interfaces they need.
For example, if we need a document that can be both printed and saved, we can create a class that implements
both the Printable and Savable interfaces.
"""
class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class Printable:
    def print(self):
        pass

class Savable:
    def save(self):
        pass

class PrintableDocument(Document, Printable):
    def print(self):
        print(f"Printing document {self.title}: {self.content}")

class SavableDocument(Document, Savable):
    def save(self):
        print(f"Saving document {self.title}: {self.content}")
