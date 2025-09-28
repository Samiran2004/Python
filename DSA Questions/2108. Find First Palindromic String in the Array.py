from typing import List
def checkPalindromeString(word: str)-> bool:
    if len(word) <= 1:
        return False
    reversedWord = word[::-1]
    return word == reversedWord

def firstPalindrome(words: List[str])-> str:
    if len(words) == 0:
        return ""
    for word in words:
        isPalindrome = checkPalindromeString(word=word)
        if isPalindrome:
            return word
    return ""

words = list()
size = int(input("Enter the size of the words array: "))
for i in range(0, size):
    data = str(input("Enter the word: "))
    words.append(data)
