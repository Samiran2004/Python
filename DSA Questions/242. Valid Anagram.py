def isAnagram(s: str, t: str)-> bool:
    if len(s) != len(t):
        return False

    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    return s == t

s = str(input("Enter the 1st string: "))
t = str(input("Enter the 2nd string: "))
print(isAnagram(s, t))