from typing import List
def threeConsecutiveOdds(nums: List[int])-> bool:
    if len(nums) < 3:
        return False
    count = 0
    flag = False
    for num in nums:
        if num % 2 != 0:
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


nums = list()
size = int(input("Enter the size of the nums array: "))
for i in range(0, size):
    data = int(input("Enter the data: "))
    nums.append(data)
print(threeConsecutiveOdds(nums=nums))
