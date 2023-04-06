class MyList(list):
    def __getattribute__(self, name):
        print(f"Getting attribute {name}")

        return super().__getattribute__(name)


my_list = MyList([1, 2, 3])
print(my_list.__len__())
