set1 = {1, 2, 3, 4}
set2 = {1, 2, 3}
set3 = {1, 2, 3, 4, 5}

print(set1 >= set2)  # True, set1 contains all elements of set2
print(set2 >= set1)  # False, set2 is not a superset of set1
print(set1 >= set3)  # False, set1 is not a superset of set3
