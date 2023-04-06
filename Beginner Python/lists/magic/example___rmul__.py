class MyList(list):
    def __rmul__(self, other):
        return self[::-1] * other

my_list = MyList([1, 2, 3])
result = 2 * my_list
print(result) # output: [3, 2, 1, 3, 2, 1]
