# Python Modules:
#   What is a Module?
#   -> A module is a file containing Python definitions, statements, functions, and classes.
#   The file name is the module name with the suffix .py added.#

# Creating a Module
def printForward(n):
    '''Print numbers from 1 to n'''
    for i in range(n):
        print(i+1)

def printBackwards(n):
    '''Print numbers from n to 1'''
    for i in range(n):
        print(n-i)