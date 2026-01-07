from typing import List

def search(nums: List[int], target: int)-> int:
    if len(nums) == 0:
        return -1
    start = 0
    end = len(nums) -1
    
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

size: int = int(input("Enter the size of the array: "))
arr: List[int] = list()

for _ in range(size):
    data: int = int(input("Enter data: "))
    arr.append(data)

target: int = int(input("Enter the target value: "))

print(search(nums=arr, target=target))