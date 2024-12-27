# Using the debugger to inspect variables
import pdb

def multiply_numbers(a, b):
    pdb.set_trace()  # Start debugging here
    result = a * b
    return result

x = 4
y = 5
print("Multiplication Result:", multiply_numbers(x, y))
