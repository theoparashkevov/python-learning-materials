class MyList(list):
    def __setitem__(self, index, value):
        print(f"Setting {value} at index {index}")
        super().__setitem__(index, value)

my_list = MyList([1, 2, 3, 4, 5])
my_list[2] = 6  # Output: Setting 6 at index 2
print(my_list)  # Output: [1, 2, 6, 4, 5]
