from typing import List
def containsDuplicateBruteForce(arr: List[int])-> bool:
    for i in range(0, len(arr)-1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def containsDuplicate(arr: List[int])-> bool:
    map = {}
    for i in range(0, len(arr)):
        if map.get(arr[i]):
            return True
        map[arr[i]] = 1
    return False

arr = list()
size = int(input("Enter the size of the array: "))
for _ in range(size):
    data = int(input("Enter the data: "))
    arr.append(data)
print(containsDuplicateBruteForce(arr=arr))
print(containsDuplicate(arr=arr))
