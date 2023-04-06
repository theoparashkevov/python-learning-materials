class MyList(list):
    def __str__(self):
        return f"My custom list: {super().__str__()}"


my_list = MyList([1, 2, 3, 4])
print(my_list)
