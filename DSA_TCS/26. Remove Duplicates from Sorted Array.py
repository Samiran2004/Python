def removeDuplicates(nums):
    if len(nums) <= 0:
        return 0
    dict_map = {}
    j = 0
    
    for i in nums:
        dict_map[i] = 0
    
    for k in dict_map:
        nums[j] = k
        j += 1
    
    return j
        
nums = []
size = int(input("Enter the size of the array: "))
for _ in range(0, size):
    data = int(input("Enter data: "))
    nums.append(data)

print(removeDuplicates(nums=nums))