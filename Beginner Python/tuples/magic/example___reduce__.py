import pickle


class MyTuple(tuple):

    def __init__(self, data):
        self.data = data

    def __reduce__(self):
        # Return a tuple containing the constructor and the tuple's arguments
        return  (self.__class__, (self.data, ))


# Create an instance of the custom tuple class
t1 = MyTuple( (1, 2, 3) )

# Pickle the instance using the dumps() method
pickled = pickle.dumps(t1)

# Unpickle the pickled representation using the loads() method
t2 = pickle.loads(pickled)

# Verify that the unpickled instance has the same elements as the original
print(t2)  # (1, 2, 3)

# Verify that the unpickled instance is an instance of the custom tuple class
print(type(t2))  # <class '__main__.MyTuple'>
