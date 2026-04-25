from typing import List
def maxSubArray(nums: List[int])-> int:
    if len(nums) <= 0:
        return 0
    maxSub = nums[0]
    currSum = 0
    for num in nums:
        if currSum < 0:
            currSum = 0
        currSum += num
        maxSub = max(currSum, maxSub)
    return maxSub

nums = list()
size = int(input("Enter the size of the array: "))

for _ in range(size):
    data = int(input("Enter the data of the array: "))
    nums.append(data)
print(maxSubArray(nums=nums))
