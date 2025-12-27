from typing import List

def reverseString(s: List[str]):
    if len(s) <= 1:
        return
    
    i = 0
    j = len(s) - 1
    
    print(f"Given string: {s}")
    
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    
    print(f"Reversed string: {s}")

user_input = input("Enter a sentence or list of words: ")
word_list = list(user_input)

reverseString(s=word_list)