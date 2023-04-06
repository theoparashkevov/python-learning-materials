class CaseInsensitiveList(list):
    def __contains__(self, item):
        for element in self:
            if str(element).lower() == str(item).lower():
                return True
        return False

# Create an instance of CaseInsensitiveList
my_list = CaseInsensitiveList(['foo', 'BAR', 'baz'])

# Test if 'Foo' is in my_list
print('Foo' in my_list)  # True

# Test if 'qux' is in my_list
print('qux' in my_list)  # False
