try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This always runs.")