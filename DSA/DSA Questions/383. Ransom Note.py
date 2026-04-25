from collections import defaultdict

def canConstruct(ransomNote: str, magazine: str)-> bool:
    d = defaultdict(int)
    
    for char in magazine:
        d[char] += 1
    for char in ransomNote:
        if d[char] <= 0:
            return False
        d[char] -= 1
    return True

ransomNote: str = str(input("Enter the string of ransomNote: "))
magazine: str = str(input("Enter the string of magazine: "))
print(canConstruct(ransomNote=ransomNote, magazine=magazine))