x = '10'

try:
    if(x > 10):
        print("Greater than 10")
    else:
        print("Less than 10")
except Exception as e:
    print("Error occurs...", e)

print(x)


def my_function(p_x):

    try:
        if(p_x % 2 == 0):
            return 1
    except Exception as e:
        return e
    finally:
        print("Hello World from the my_function")

print(my_function("4"))

x = 10
if x < 100:
    raise ValueError("Value < 100 is not allowed")