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