def wordPattern(pattern: str, s: str)-> bool:
    words = s.split(" ")
    l = len(words)
    if l != len(pattern):
        return False
    i = 0
    d = {}
    while i<l:
        if pattern[i] in d and d[pattern[i]] != words[i]:
            return False
        else:
            d[pattern[i]] = words[i]
        i += 1
    
    c = set()
    for char in pattern:
        c.add(char)
    
    d = set(words)
    
    if len(c) != len(d):
        return False
    return True

pattern: str = str(input("Enter the pattern string: "))
s: str = str(input("Enter the string: "))
print(wordPattern(pattern=pattern, s=s))