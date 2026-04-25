from collections import defaultdict, Counter

def findTheDifference(s: str, t: str)-> str:
    if len(s) == 0:
        return t
    elif len(t) == 0:
        return s
    count_s, count_t = Counter(s), Counter(t)
    
    for c in count_t:
        if c not in count_s:
            return c
        if count_s[c] < count_t[c]:
            return c

s: str = str(input("Enter the 1st string: "))
t: str = str(input("Enter the 2nd string: "))
print(findTheDifference(s=s, t=t))