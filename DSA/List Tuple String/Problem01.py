def runningSum(nums):
    if len(nums) == 0:
        return []
    resultArr = [nums[0]]
    if len(nums) != 0:
        for i in range(1, len(nums)):
            resultArr.append(resultArr[i-1] + nums[i])

    return resultArr


size = int(input("Enter the size of the array: "))
arr = []
for i in range(0, size):
    data = int(input("Enter the data: "))
    arr.append(data)
print(arr)
result = runningSum(arr)
print(result)