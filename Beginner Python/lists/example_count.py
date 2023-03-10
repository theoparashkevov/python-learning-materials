example_list = [1, 2, 2, 3, 3, 3, 'a', 'b', 'c', 'X', 'Y', 'Z']
print(example_list)

count_1s = example_list.count(1)
print('Amount of 1s in the list: ', count_1s)

count_2s = example_list.count(2)
print('Amount of 2s in the list: ', count_2s)

count_3s = example_list.count(3)
print('Amount of 3s in the list: ', count_3s)

count_as = example_list.count('a')
print("Amount of a's in the list: ", count_as)

count_bs = example_list.count('b')
print("Amount of b's in the list: ", count_bs)

count_cs = example_list.count('c')
print("Amount of c's in the list: ", count_cs)

count_Xs = example_list.count('X')
print("Amount of c's in the list: ", count_cs)

count_Ys = example_list.count('Y')
print("Amount of c's in the list: ", count_cs)

count_Zs = example_list.count('Z')
print("Amount of c's in the list: ", count_cs)

# Cannot count type of variable here like this
count_ints = example_list.count(int)
print("Amount of int's in the list: ", count_ints)

# Cannot count type of variable here like this
count_type_ints = example_list.count(type(int))
print("Amount of type int's in the list: ", count_type_ints)