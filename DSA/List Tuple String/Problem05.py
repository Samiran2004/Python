def maxSubArray(nums):
    n = len(nums)

    max_sum = nums[0]
    curr_sum = 0

    for i in range(n):
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

size = int(input("Enter the size of the array: "))
arr = []
for i in range(0, size):
    data = int(input("Enter data: "))
    arr.append(data)

print(maxSubArray(arr))