"""
In this example, we create a new context for starting processes using the get_context()
function from the multiprocessing module. We specify the 'forkserver' context,
which is used on Unix-based systems and provides a more efficient way of creating new processes
compared to the 'fork' context.

We then create a new Process object and specify that we want to execute the print_numbers()
function in the new process by passing it as the target argument. However,
this time we use the context's Process method instead of the multiprocessing.Process method.

We then start the process using the start() method and wait for it to complete using the join() method.
When the process runs, it will execute the print_numbers() function in parallel with the main process,
allowing the numbers to be printed simultaneously.

Note that the 'forkserver' context is only available on Unix-based systems and requires Python 3.4 or later.
If you're using an older version of Python or a different operating system, this context may not be available.
"""


import multiprocessing

# Define a function to be executed in parallel
def print_numbers():
    for i in range(1, 11):
        print(i)

# Create a new context for starting processes
ctx = multiprocessing.get_context('forkserver')

# Create a new process that will execute the function
p = ctx.Process(target=print_numbers)

# Start the process
p.start()

# Wait for the process to complete
p.join()

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
