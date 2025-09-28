from typing import List

def calculateSumOfDigits(nums: List[int])-> int:
    if len(nums) == 0:
        return 0
    sum = 0
    for num in nums:
        n = num
        while n != 0:
            rem = n % 10
            sum += rem
            n = n // 10
    return sum

def calculateSumOfNums(nums: List[int])-> int:
    if len(nums) == 0:
        return 0
    sum = 0
    for num in nums:
        sum += num
    return sum

def differenceOfSum(nums: List[int])-> int:
    sumOfDigits = calculateSumOfDigits(nums=nums)
    sumOfNums = calculateSumOfNums(nums=nums)
    return sumOfNums - sumOfDigits

nums = list()
size = int(input("Enter the size of the nums array: "))
for i in range(0, size):
    data = int(input("Enter the number: "))
    nums.append(data)

print(differenceOfSum(nums=nums))
