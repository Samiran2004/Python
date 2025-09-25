x = 10

def foo():
    global x
    x = x + 10
    print(x)

print(f"Global value: {x}")
foo()