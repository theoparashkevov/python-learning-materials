import multiprocessing

# Define a function to be executed in parallel
def print_numbers():
    for i in range(1, 11):
        print(i)

# Create a new context for starting processes
ctx = multiprocessing.get_context('spawn')

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
