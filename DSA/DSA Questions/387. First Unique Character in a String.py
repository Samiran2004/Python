from collections import defaultdict

def firstUniqChar(s: str)-> int:
    S: list = list(s)
    
    if len(S) <= 0:
        return -1
    
    count = defaultdict(int)
    
    for char in S:
        count[char] += 1
    
    for i, c in enumerate(S):
        if count[c] == 1:
            return i
    return -1

s: str = str(input("Enter the string: "))
print(firstUniqChar(s=s))