import math

def greet(name):
    """This function greets the person passed in as a parameter"""
    print(f"Hello, {name}")

name = input("Enter your name: ")
greet(name)

def add(x, y):
    return x + y

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
result = add(x, y)
print(result)

num = int(input("Enter the number to calculate sqrt: "))
print(math.sqrt(num))




## Function with default parameter...
def greet(name="Samiran"):
    print(name)
greet()
greet("Guddu")

## OS module...
import os
print(f"Current directory: {os.getcwd()}")
for file in os.listdir():
    print(file)

## sys module...
import sys
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

## subprocess module...
import subprocess
output = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(output.stdout)