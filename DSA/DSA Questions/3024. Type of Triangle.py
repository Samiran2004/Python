from typing import List
def triangleType(nums: List[int])-> str:
    if not is_triangle(nums):
        return "none"
    if is_equilateral(nums):
        return "equilateral"
    if is_isosceles(nums):
        return "isosceles"
    return "scalene"

def is_triangle(nums: List[int])-> bool:
    return(
        nums[0] + nums[1] > nums[2] and
        nums[0] + nums[2] > nums[1] and
        nums[1] + nums[2] > nums[0]
    )

def is_equilateral(nums: List[int])-> bool:
    return nums[0] == nums[1] == nums[2]

def is_isosceles(nums: List[int])-> bool:
    return nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]

nums = list()
size = int(input("Enter the size of the nums array: "))
for i in range(0, size):
    data = int(input("Enter the data: "))
    nums.append(data)
print(triangleType(nums=nums))
