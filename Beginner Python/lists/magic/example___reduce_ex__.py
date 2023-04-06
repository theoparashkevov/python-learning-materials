class MyList(list):
    def __reduce_ex__(self, protocol):
        return type(self), (list(self),) # Return the class and the state as a tuple

# Create an instance of MyList
my_list = MyList([1, 2, 3, 4])

# Serialize the object using pickle.dumps
import pickle
serialized = pickle.dumps(my_list)

# Deserialize the object using pickle.loads
deserialized = pickle.loads(serialized)

# Verify that the deserialized object is equal to the original object
assert my_list == deserialized

print(my_list == deserialized)
