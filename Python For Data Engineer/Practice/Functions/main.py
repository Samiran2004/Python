def myFunction(x=20):
    if(x > 10):
        print("Greater than 10")
    else:
        print("IDK")

myFunction(10)
myFunction()
myFunction(20)

def myFunction2(*x):
    print(x, type(x))

myFunction2(10, 20, 30, 40)

def myFunction3(**x):
    print(x)

myFunction3(x=10, y=20, z=30)