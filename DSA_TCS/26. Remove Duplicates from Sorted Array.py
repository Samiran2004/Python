def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[write_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index

nums = []
size = int(input("Enter the size of the array: "))
for _ in range(0, size):
    data = int(input("Enter data: "))
    nums.append(data)

print(removeDuplicates(nums=nums))
