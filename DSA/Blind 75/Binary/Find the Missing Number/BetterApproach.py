from typing import List


class BetterApproachSolution:
    def missingNum(self, arr: List[int]):
        n = len(arr) + 1
        hash = [0] * (n + 1)
        
        for i in range(n-1):
            hash[arr[i]] += 1
        
        for i in range(1, n+1):
            if hash[i] == 0:
                return i
        
        return -1