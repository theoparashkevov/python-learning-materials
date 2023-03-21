"""
In this example, we first define a simple function print_numbers() that will print numbers from 1 to 10. We then create
a new Process object and specify that we want to execute the print_numbers() function in the new process by passing
it as the target argument.

We then start the process using the start() method and wait for it to complete using the join() method. When the process
runs, it will execute the print_numbers() function in parallel with the main process, allowing the numbers to be
printed simultaneously.
"""
import multiprocessing

# Define a function to be executed in parallel
def print_numbers():
    for i in range(1, 11):
        print(i)

# Create a new process that will execute the function
p = multiprocessing.Process(target=print_numbers)

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
