class MyList(list):
    def __format__(self, format_spec):
        if format_spec == 'pretty':
            return '\n'.join(str(item) for item in self)
        elif format_spec == 'csv':
            return ','.join(str(item) for item in self)
        else:
            return super().__format__(format_spec)

my_list = MyList([1, 2, 3])

# Format my_list as a "pretty" string
pretty_string = format(my_list, 'pretty')
print(pretty_string)

# Format my_list as a CSV string
csv_string = format(my_list, 'csv')
print(csv_string)

# Format my_list using the default string format
default_string = format(my_list)
print(default_string)
