########################################################################################################################
#                                                EXAMPLE 1
########################################################################################################################
def simple_decorator_1(f):
    def wrapper(*args, **kwargs):
        # Do something
        print('[Wrapper] Positional Arguments: ', args)
        print('[Wrapper] Keyword Arguments: ', kwargs)

        # Run the function
        function_result = f(*args, **kwargs)

        # Do something on result
        function_result += 0

        return function_result

    return wrapper


@simple_decorator_1
def simple_add_function_1(a: int, b: int) -> int:
    # simple_decorator(simple_add_function)
    # wrapper       ->  (a, b)
    return a + b


def example_1():
    int_a = 10
    int_b = 20

    print('Using positional arguments')
    result = simple_add_function_1(int_a, int_b)
    print('Final result: ', result, '\n')

    print('Using Keyword arguments')
    result = simple_add_function_1(a=int_a, b=int_b)
    print('Final result: ', result, '\n')


########################################################################################################################
#                                                EXAMPLE 2
########################################################################################################################
def simple_decorator_2(*decorator_args, **decorator_kwargs):
    # there is a function to be 'decorated'
    # function => decorator_args[0]

    def wrapper(*args, **kwargs):
        print('[Decorator] Positional Arguments: ', decorator_args)
        print('[Decorator] Keyword Arguments: ', decorator_kwargs)

        # Do something
        print('[Wrapper] Positional Arguments: ', args)
        print('[Wrapper] Keyword Arguments: ', kwargs)

        # Run the function
        # function_result = f(*args, **kwargs)

        # Do something on result
        function_result = 0

        return function_result

    return wrapper


@simple_decorator_2
def simple_add_function_2(a: int, b: int) -> int:
    # simple_decorator(simple_add_function)
    # wrapper       ->  (a, b)
    return a + b


def example_2():
    int_a = 10
    int_b = 20

    print('Using positional arguments')
    result = simple_add_function_2(int_a, int_b)
    print('Final result: ', result, '\n')

    print('Using Keyword arguments')
    result = simple_add_function_2(a=int_a, b=int_b)
    print('Final result: ', result, '\n')


########################################################################################################################
#                                                EXAMPLE 3
########################################################################################################################
def simple_decorator_3(*decorator_args, **decorator_kwargs):
    # there is a function to be 'decorated'

    def decorator(f):
        def wrapper(*function_args, **function_kwargs):
            # Do something
            print('[Decorator] Positional Arguments: ', decorator_args)
            print('[Decorator] Keyword Arguments: ', decorator_kwargs)

            print('[Decorator] Function: ', f)

            print('[Wrapper] Positional Arguments: ', function_args)
            print('[Wrapper] Keyword Arguments: ', function_kwargs)

            # Run the function
            function_result = f(*function_args, **function_kwargs)

            # Do something on result
            function_result += 0

            return function_result

        return wrapper

    return decorator


@simple_decorator_3('ARG_1', 'ARG_2')
def simple_add_function_3(a: int, b: int) -> int:
    # simple_decorator(simple_add_function)
    # wrapper       ->  (a, b)
    return a + b


def example_3():
    int_a = 10
    int_b = 20

    print('Using positional arguments')
    result = simple_add_function_3(int_a, int_b)
    print('Final result: ', result, '\n')

    print('Using Keyword arguments')
    result = simple_add_function_3(a=int_a, b=int_b)
    print('Final result: ', result, '\n')


########################################################################################################################
#                                                EXAMPLE 4
########################################################################################################################
def simple_decorator_4_1(*decorator_args, **decorator_kwargs):
    # there is a function to be 'decorated'

    def decorator(f):
        def wrapper(*function_args, **function_kwargs):
            # Do something
            print('[Decorator (4_1) ] Positional Arguments: ', decorator_args)
            print('[Decorator (4_1) ] Keyword Arguments: ', decorator_kwargs)

            print('[Decorator (4_1) ] Function: ', f)

            print('[Wrapper (4_1) ] Positional Arguments: ', function_args)
            print('[Wrapper (4_1) ] Keyword Arguments: ', function_kwargs)

            # Run the function
            function_result = f(*function_args, **function_kwargs)

            # Do something on result
            function_result += 0

            return function_result

        return wrapper

    return decorator


def simple_decorator_4_2(*decorator_args, **decorator_kwargs):
    # there is a function to be 'decorated'

    def decorator(f):
        def wrapper(*function_args, **function_kwargs):
            # Do something
            print('[Decorator (4_2) ] Positional Arguments: ', decorator_args)
            print('[Decorator (4_2)] Keyword Arguments: ', decorator_kwargs)

            print('[Decorator (4_2)] Function: ', f)

            print('[Wrapper (4_2) ] Positional Arguments: ', function_args)
            print('[Wrapper (4_2) ] Keyword Arguments: ', function_kwargs)

            # Run the function
            function_result = f(*function_args, **function_kwargs)

            # Do something on result
            function_result += 0

            return function_result

        return wrapper

    return decorator


@simple_decorator_4_2('DECORATOR_4_2_ARG_1', 'DECORATOR_4_2_ARG_2')
@simple_decorator_4_1('DECORATOR_4_1_ARG_1', 'DECORATOR_4_1_ARG_2')
def simple_add_function_4(a: int, b: int) -> int:
    # simple_decorator(simple_add_function)
    # wrapper       ->  (a, b)
    return a + b


def example_4():
    int_a = 10
    int_b = 20

    print('Using positional arguments')
    result = simple_add_function_4(int_a, int_b)
    print('Final result: ', result, '\n')

    print('Using Keyword arguments')
    result = simple_add_function_4(a=int_a, b=int_b)
    print('Final result: ', result, '\n')


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
    list_of_example_functions = [example_1, example_2, example_3, example_4]

    for idx, function_name in enumerate(list_of_example_functions):
        print_message(f'\t\t\tExample {idx + 1}')
        function_name()
