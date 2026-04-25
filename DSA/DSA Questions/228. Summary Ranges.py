from typing import List
def summaryRanges(nums: List[int])-> List[str]:
    ans = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
            i += 1
        if start != nums[i]:
            ans.append(str(start) + "->" + str(nums[i]))
        else:
            ans.append(str(nums[i]))
        i += 1
    return ans

nums = []
size = int(input("Enter the size of the nums array: "))
for i in range(0, size):
    data = int(input("Enter the data: "))
    nums.append(size)
