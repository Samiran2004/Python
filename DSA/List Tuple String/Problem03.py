def removeDuplicatesII(nums):
    n = len(nums)

    if n <= 2:
        return

    start = 1
    for i in range(2, n):
        if nums[i] != nums[start - 1]:
            start += 1
            nums[start] = nums[i]

    return start + 1

size = int(input("Enter the size: "))
arr = []
for i in range(0, size):
    data = int(input("Enter data: "))
    arr.append(data)