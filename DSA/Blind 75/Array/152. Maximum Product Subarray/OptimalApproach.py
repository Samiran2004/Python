from typing import List


class OptimalApproachSolution:
    def maxProduct(self, arr: List[int]):
        res = arr[0]
        maxProd = arr[0]
        minProd = arr[0]
        
        for i in range(1, len(arr)):
            curr = arr[i]
            if curr < 0:
                maxProd, minProd = minProd, maxProd
            
            maxProd = max(curr, maxProd * curr)
            minProd = min(curr, minProd * curr)
            res = max(res, maxProd)
        
        return res