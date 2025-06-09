def add(a, b):
    return a + b

print(add(5,6))


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speek(self):
        return f"{self.name} makes a sound."

dog = Animal("Dog")
dog.speek()