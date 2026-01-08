def gcdOfStrings(str1: str, str2: str)-> str:
    len1, len2 = len(str1), len(str2)
    
    def isDivisor(l):
        if len1 % l or len2 % l:
            return False
        
        f1, f2 = len1//l, len2//l
        return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
    
    for l in range(min(len1, len2), 0, -1):
        if isDivisor(l):
            return str1[:l]
    return ""

import math
def gcdOfStringsEasy(str1: str, str2: str)-> str:
    if str1 + str2 != str2 + str1:
        return ""
    max_len = math.gcd(len(str1), len(str2))
    return str1[:max_len]

str1: str = str(input("Enter the value of string1: "))
str2: str = str(input("Enter the value of string2: "))
print(gcdOfStrings(str1=str1, str2=str2))
print(gcdOfStringsEasy(str1=str1, str2=str2))