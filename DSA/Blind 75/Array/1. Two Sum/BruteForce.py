from typing import List

class Solution_Brute_Force:
    def twoSum(self, arr: List[int], target: int):
        if len(arr) <= 1:
            return "NO"
    
        for i in range(0, len(arr)-1):
            sum = 0
            for j in range(i+1, len(arr)):
                sum = arr[i] + arr[j]
                if sum == target:
                    return "YES"    
        return "NO"