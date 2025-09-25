def sortArrayByParity(nums):
    n = len(nums)
    if n <= 1:
        return nums
    start = 0
    for i in range(n):
        if nums[i] % 2 == 0:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start += 1
    return arr


size = int(input("Enter the size: "))
arr = []
for i in range(0, size):
    data = int(input("Enter data: "))
    arr.append(data)

print(arr)
arr = sortArrayByParity(arr)
print(arr)