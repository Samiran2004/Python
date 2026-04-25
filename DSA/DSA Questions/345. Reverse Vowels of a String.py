def reverseVowels(s: str)-> str:
    S = list(s)
    if len(s) <= 1:
        return s
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    left, right = 0, len(s) - 1
    
    while left < right:
        if S[left] not in vowels:
            left += 1
        elif S[right] not in vowels:
            right -= 1
        else:
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1
    return ''.join(S)

s: str = str(input("Enter the string: "))
print(reverseVowels(s=s))