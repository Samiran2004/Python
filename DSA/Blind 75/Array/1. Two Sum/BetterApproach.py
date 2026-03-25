from typing import List


class SolutionBetterApproach:
    def twoSum(self, arr: List[int], target: int):
        map = {}
        
        for i, num in enumerate(arr):
            complement = target - num
            
            if complement in map:
                return "YES"
            
            map[num] = i
        
        return "NO"