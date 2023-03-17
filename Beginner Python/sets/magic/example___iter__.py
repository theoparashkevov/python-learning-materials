class ReverseSet(set):
    def __iter__(self):
        return reversed(list(super().__iter__()))

my_set = ReverseSet([1, 2, 3, 4, 5])
for i in my_set:
    print(i)
