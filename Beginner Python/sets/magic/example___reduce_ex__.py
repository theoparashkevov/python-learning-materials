
class MySet(set):
    def __reduce_ex__(self, protocol):
        return type(self), (list(self),) # Return the class and the state as a tuple

# Create an instance of MySet
myset = MySet([1, 2, 3, 4])

# Serialize the object using pickle.dumps
import pickle
serialized = pickle.dumps(myset)

# Deserialize the object using pickle.loads
deserialized = pickle.loads(serialized)

# Verify that the deserialized object is equal to the original object
assert myset == deserialized

print(myset == deserialized)
