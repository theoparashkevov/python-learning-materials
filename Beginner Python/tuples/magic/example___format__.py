class MyTuple(tuple):
    def __format__(self, format_spec):
        if format_spec == "":
            return str(self)
        else:
            return ", ".join(format(v, format_spec) for v in self)

my_tuple = MyTuple((1, 2, 3))

print("{:}", my_tuple)
print("{:10}", my_tuple)
print("{:02X}", my_tuple)
