import os
import sys

v_list = list()
v_tuple = tuple()
v_set = set()
v_dict = dict()


########################################################################################################################
#                                                LIST
########################################################################################################################
def add_elements_to_a_list():
    tmp_list = list()

    tmp_list.append('a')
    tmp_list.append('b')
    tmp_list.append('c')

    print(tmp_list)


def add_two_lists_together():
    tmp_list_1 = list()
    tmp_list_2 = list()

    tmp_list_1.append('a1')
    tmp_list_1.append('b1')
    tmp_list_1.append('c1')

    tmp_list_2.append('a2')
    tmp_list_2.append('b2')
    tmp_list_2.append('c2')

    print('List 1 ', tmp_list_1)
    print('List 2 ', tmp_list_2)

    result_list = tmp_list_1 + tmp_list_2
    # equivalent to
    # result_list = tmp_list_1.__add__(tmp_list_2)

    print('Resulting List ', result_list)


def example_list():
    print('\n', 'Add Elements to a list')
    add_elements_to_a_list()

    print('\n', 'Add Two Lists together')
    add_two_lists_together()


########################################################################################################################
#                                                TUPLE
########################################################################################################################


if __name__ == "__main__":
    example_list()
