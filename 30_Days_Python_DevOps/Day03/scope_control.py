x = 10

def changeValue():
    global x
    x = 20

print(x) # 10
changeValue()
print(x) # 20


def outer():
    y = "outer"

    def inner():
        nonlocal y
        y = "inner"
        print("Inner Y value: ", y)

    inner()
    print("Outer Y value: ", y)

outer()