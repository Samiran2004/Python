from typing import List

def topKFrequent(nums: List[int], k: int)-> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

nums = list()
size = int(input("Enter the size of the array: "))

for _ in range(size):
    data = int(input("Enter the data of the array: "))
    nums.append(data)

k = int(input("Enter the value of K: "))

print(topKFrequent(nums=nums, k=k))
