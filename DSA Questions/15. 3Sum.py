from typing import List

def threeSumBruteForce(nums: List[int], target: int)-> List[List[int]]:
    n = len(nums)
    my_set = set()
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1 , n):
                if arr[i] + arr[j] + arr[k] == target:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    my_set.add(tuple(temp))
    return [list(ans) for ans in my_set]

def threeSum(nums: List[int])-> List[List[int]]:
    res = set()
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.add(tuple([nums[i], nums[left], nums[right]]))
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return [list(ans) for ans in res]

size: int = int(input("Enter the size of the array: "))
arr: List[int] = list()
for _ in range(size):
    data: int = int(input("Enter data: "))
    arr.append(data)
target: int = int(input("Enter the value of target: "))
print(threeSumBruteForce(nums=arr, target=target))
print(threeSum(nums=arr))