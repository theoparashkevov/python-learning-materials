class MyList(list):
    def __setattr__(self, name, value):
        if name == 'size':
            self.append(value)
        else:
            super().__setattr__(name, value)

# Example usage:
lst = MyList([1, 2, 3])
lst.size = 4
print(lst) # Output: [1, 2, 3, 4]
