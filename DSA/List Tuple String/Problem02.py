def removeDuplicates(nums):
    n = len(nums)
    start = 0
    for i in range(1, n):
        if nums[i] != nums[start]:
            start += 1
            nums[start] = nums[i]
    return start+1


size = int(input("Enter the size of the array: "))
arr = []
for i in range(0, size):
    data = int(input("Enter data: "))
    arr.append(data)
print(arr)
result = removeDuplicates(arr)
print(result)