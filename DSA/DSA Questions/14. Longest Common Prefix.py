from typing import List
def longestCommonPrefix(strs: List[str])-> str:
    if len(strs) == 0:
        return ""
    resStr = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return resStr
        resStr += strs[0][i]
    return resStr

arr = list()
size = int(input("Enter the size of the arr: "))
for _ in range(0, size):
    data = str(input("Enter the string: "))
    arr.append(data)

print(longestCommonPrefix(strs=arr))
