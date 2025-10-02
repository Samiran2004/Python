def theMaximumAchievableX(num: int, t: int)-> int:
    return num + 2 * t

num = int(input("Enter the number: "))
t = int(input("Enter the value of t: "))
print(theMaximumAchievableX(num=num, t=t))
