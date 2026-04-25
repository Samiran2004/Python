from typing import List
def canAliceWin(nums: List[int])-> bool:
    singleDigitSum = 0
    doubleDigitSum = 0
    for i in nums:
        if i < 10:
            singleDigitSum += i
        else:
            doubleDigitSum += i
    return singleDigitSum != doubleDigitSum

nums = list()
size = int(input("Enter the size of the nums array: "))
for i in range(0, size):
    data = int(input("Enter the data: "))
    nums.append(data)

print(canAliceWin(nums=nums))
