import pickle

class CustomList(list):
    def __reduce__(self):
        return (self.__class__, (list(self),))


custom_list = CustomList([1, 2, 3])
serialized = pickle.dumps(custom_list)
deserialized = pickle.loads(serialized)
print(deserialized)  # Output: [1, 2, 3]
print(type(deserialized))  # Output: <class '__main__.CustomList'>
