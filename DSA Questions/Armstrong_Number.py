def isArmstrongNumber(num: int)-> bool:
    str_num = str(num)
    length = len(str_num)

    n = num
    result = 0
    while n != 0:
        rem = n % 10
        result += rem ** length
        n = n//10

    if result == num:
        return True
    return False


num = int(input("Enter the number: "))
print(isArmstrongNumber(num=num))
