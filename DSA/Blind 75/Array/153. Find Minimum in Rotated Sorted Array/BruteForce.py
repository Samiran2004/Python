from typing import List


class BruteForceSolution:
    def findMin(self, arr: List[int]):
        min_val = float('inf')
        
        for i in range(len(arr)):
            min_val = min(min_val, arr[i])
        
        return min_val