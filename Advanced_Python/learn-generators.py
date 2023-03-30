from sys import getsizeof


########################################################################################################################
#                                                EXAMPLE 1
########################################################################################################################
def generator_1(upper_limit):
    n = 0

    while n <= upper_limit:
        if n % 20:
            print(n, end=' ')
        else:
            print(n, end='\n')

        yield n
        n += 1

    print(end='\n')


def example_1(ul=100):
    # upper_limit_arg = ul
    upper_limit_arg = 2**(getsizeof(int) - 1)
    result = sum(generator_1(upper_limit_arg))

    print('Size of Integer = ', getsizeof(int))
    print('Result: ', result)
    return result


########################################################################################################################
#                                                MAIN
########################################################################################################################

def print_decorator(sep_string: str, sep_string_len: int):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print('\n\n\n')
            print(sep_string * sep_string_len)
            f(*args, **kwargs)
            print(sep_string * sep_string_len)

        return wrapper

    return decorator


@print_decorator(sep_string='#', sep_string_len=40)
def print_message(*args, **kwargs):
    # print_decorator(sep_string='#', sep_string_len=40)
    # decorator ->      (print_message)
    # wrapper   ->      (*args, **kwargs)
    print(*args, **kwargs)


if __name__ == "__main__":
    list_of_example_functions = [example_1]

    for idx, function_name in enumerate(list_of_example_functions):
        print_message(f'\t\t\tExample {idx + 1}')
        function_name()
