"""Lambda Function"""
"""What is Lambda Function?
    => A lambda function is a small anonymous function that can take any number of
        arguments but can only have one expression."""
    
def add(x, y):
    return x + y

print(add(5, 3))

add = lambda x, y: x + y
print(add(5, 3))