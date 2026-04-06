from typing import List


class OptimalApproachSolution:
    def maxSubArray(self, arr: List[int]):
        maxi = float('-inf')
        sum = 0
        
        for i in range(len(arr)):
            sum += arr[i]
            
            if sum > maxi:
                maxi = sum
            
            if sum < 0:
                sum = 0
        
        return maxi