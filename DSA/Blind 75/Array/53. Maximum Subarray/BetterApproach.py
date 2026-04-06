from typing import List


class BetterApproachSolution:
    def maxSubArray(self, arr: List[int]):
        maxi = float('-inf')
        for i in range(len(arr)):
            sum = 0
            for j in range(i, len(arr)):
                sum += arr[j]
                
                maxi = max(maxi, sum)
        
        return maxi