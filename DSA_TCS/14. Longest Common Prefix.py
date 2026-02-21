from typing import List
def longestCommonPrefix(strs: List[str])-> str:
    if not strs:
        return ""
    result = ""
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if i == len(word) or word[i] != base[i]:
                return result
        result += base[i]
    return result

try:
    size = int(input("Enter the size of the list: "))
    strs = []
    for _ in range(size):
        data = str(input("Enter the string: "))
        strs.append(data)
except ValueError:
    print("Please enter a valid number of the size.")

print(longestCommonPrefix(strs=strs))