
import pickle

class MySet(set):
    def __reduce__(self):
        return (set, (list(self),))

s = MySet([1, 2, 3])
serialized_data = pickle.dumps(s)
deserialized_set = pickle.loads(serialized_data)
print(deserialized_set) # Output: {1, 2, 3}
