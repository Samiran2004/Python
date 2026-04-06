from typing import List


class BruteForceSolution:
    def maxSubArray(self, arr: List[int]):
        max_sum = float('-inf')
        
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                sum = 0
                for k in range(i, j+1):
                    sum += arr[k]
                
                max_sum = max(sum, max_sum)
        
        return max_sum