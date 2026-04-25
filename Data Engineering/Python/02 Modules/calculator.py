"""Calculator module with basic math operations"""

def add(a, b):
    """Add two numbers"""
    return a+b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply  two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Module-level variable
PI = 3.14159

# Test code
if __name__ == '__main__':
    print("Testing calculator module...")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"5 / 3 = {divide(5, 3)}")