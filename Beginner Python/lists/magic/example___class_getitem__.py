class MyList(list):
    def __class_getitem__(cls, item):
        if item == int:
            return IntList
        elif item == str:
            return StrList
        else:
            return cls

class IntList(MyList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._validate()

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError("IntList can only contain integers")
        super().append(value)
        self._validate()

    def extend(self, values):
        for value in values:
            if not isinstance(value, int):
                raise TypeError("IntList can only contain integers")
        super().extend(values)
        self._validate()

    def _validate(self):
        for value in self:
            if not isinstance(value, int):
                raise TypeError("IntList can only contain integers")

class StrList(MyList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._validate()

    def append(self, value):
        if not isinstance(value, str):
            raise TypeError("StrList can only contain strings")
        super().append(value)
        self._validate()

    def extend(self, values):
        for value in values:
            if not isinstance(value, str):
                raise TypeError("StrList can only contain strings")
        super().extend(values)
        self._validate()

    def _validate(self):
        for value in self:
            if not isinstance(value, str):
                raise TypeError("StrList can only contain strings")

# Create an instance of MyList
my_list = MyList[int]([1, 2, 3])

# Print the type of my_list
print(type(my_list))  # <class '__main__.IntList'>

# Try to add a non-integer to my_list
try:
    my_list.append('four')
except TypeError as e:
    print(e)  # IntList can only contain integers
