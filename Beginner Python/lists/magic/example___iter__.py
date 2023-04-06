class MyList:
    def __init__(self, elements):
        self.elements = elements

    def __iter__(self):
        print("Iterating")
        return iter(self.elements)

my_list = MyList([1, 2, 3, 4, 5])

for element in my_list:
    print(element)
