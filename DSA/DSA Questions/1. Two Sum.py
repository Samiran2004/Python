from typing import List
def twoSumBruteForce(nums: List[int], target: int)-> List[int]:
    ans = []
    for i in range(0, len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
                return ans
    return ans

def twoSum(nums: List[int], target: int)-> List[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap: 
            return [prevMap[diff], i]
        prevMap[n] = i
    return []

arr = list()
size = int(input("Enter the size of the array: "))
for _ in range(size):
    data = int(input("Enter data: "))
    arr.append(data)

key = int(input("Enter the key data: "))
print(twoSumBruteForce(nums=arr, target=key))
print(twoSum(nums=arr, target=key))
