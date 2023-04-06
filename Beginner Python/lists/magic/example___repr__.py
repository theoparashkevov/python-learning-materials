class MyList(list):
    def __repr__(self):
        return f"MyList({super().__repr__()})"

my_list = MyList([1, 2, 3])
print(my_list) # output: MyList([1, 2, 3])
