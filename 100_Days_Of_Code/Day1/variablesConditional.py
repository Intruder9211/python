# Conditional variables and debugging
name = input("Enter your name: ")
if len(name) < 3:
    print("Name is too short!")
else:
    print(f"Hello, {name}!")

# Debugging the condition
import pdb
pdb.set_trace()
if len(name) > 10:
    print("That's a long name!")
