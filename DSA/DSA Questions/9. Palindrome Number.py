def isPalindrome(x: int)-> bool:
    if x < 0:
        return False
    
    if x != 0 and x % 10 == 0:
        return False
    n = x
    rev = 0
    
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    
    return x == rev

x: int = int(input("Enter the value: "))
print(isPalindrome(x=x))