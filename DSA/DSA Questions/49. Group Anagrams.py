from typing import List
from collections import defaultdict
def groupAnagrams(strs: List[str])-> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)

    return list(res.values())

arr = list()
size = int(input("Enter the size of the array: "))
for _ in range(size):
    data = str(input("Enter the data of the array: "))
    arr.append(data)
print(groupAnagrams(strs=arr))
