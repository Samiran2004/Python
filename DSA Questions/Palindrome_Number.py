def checkPalindrome(num: int) -> bool:
    if num < 0:
        return False
    if num < 10:
        return True

    revNum = 0
    n = num
    while n != 0:
        rem = n % 10
        revNum = revNum + rem
        n = n // 10

        if n != 0:
            revNum = revNum * 10

    return num == revNum

num = int(input("Enter the number: "))
print(f"The number is {num}")
print(f"The number {num} is palindrome: {checkPalindrome(num=num)}")
