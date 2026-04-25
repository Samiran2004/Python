def countKeyChanges(s: str)-> int:
    n = len(s)
    s = s.lower()
    changes = 0
    for i in range(0, n-1):
        if s[i] != s[i+1]:
            changes += 1
    return changes

s = str(input("Enter the string: "))
print(countKeyChanges(s=s))
