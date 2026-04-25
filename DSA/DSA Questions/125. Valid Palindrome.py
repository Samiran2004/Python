def isPalindrome(s: str)-> bool:
    if len(s) == 0:
        return False
    if s == " ":
        return True
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    print(newStr)
    reversedStr = newStr[::-1]
    print(reversedStr)
    return newStr == reversedStr

s = str(input("Enter the string: "))
print(isPalindrome(s=s))
