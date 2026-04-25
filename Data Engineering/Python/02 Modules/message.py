"""This is the message module documentation"""

def welcome(name):
    print(f"Hi {name}. Welcome to Python.")
    
def bye(name):
    print(f"Good Bye {name}. See you again")

if __name__ == '__main__':
    # This code runs only when module is executed directly
    name = input("Enter your name: ")
    welcome(name=name)