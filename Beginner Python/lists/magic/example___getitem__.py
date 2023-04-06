class MyList(list):
    def __getitem__(self, index):
        print(f"Getting item at index {index}")
        return super().__getitem__(index)

my_list = MyList([1, 2, 3])
print(my_list[0])
