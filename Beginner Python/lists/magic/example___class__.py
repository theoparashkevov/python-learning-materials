class MyList(list):
    def __class__(self):
        return str

# Create an instance of MyList
my_list = MyList([1, 2, 3])

# Check the class of my_list
print(type(my_list))  # <class 'str'>
