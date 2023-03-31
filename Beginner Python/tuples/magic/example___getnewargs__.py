import pickle

my_tuple = (1, 2, 3, 4, 5)
new_tuple = pickle.loads(pickle.dumps(my_tuple))

print(my_tuple)  # (1, 2, 3, 4, 5)
print(new_tuple)  # (1, 2, 3, 4, 5)
print(my_tuple == new_tuple)  # True
print(my_tuple is new_tuple)  # False
