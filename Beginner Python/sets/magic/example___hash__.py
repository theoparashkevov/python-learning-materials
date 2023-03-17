class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)

person_set = set()
person_set.add(Person('Alice', 25))
person_set.add(Person('Bob', 30))
person_set.add(Person('Alice', 25))  # Adding duplicate object

print(person_set)  # Output: {<__main__.Person object at 0x7f09db04b0a0>, <__main__.Person object at 0x7f09db04b160>}
