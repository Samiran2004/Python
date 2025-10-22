from typing import List

def productExceptSelf(nums: List[int])-> List[int]:
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

nums = list()
size = int(input("Enter the size of the array: "))

for _ in range(size):
    data = int(input("Enter the data of the array: "))
    nums.append(data)

print(productExceptSelf(nums=nums))
