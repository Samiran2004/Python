from typing import List


class BruteForceSolution:
    def maxProduct(self, arr: List[int]):
        max_product = arr[0]
        
        for i in range(len(arr)):
            prod = 1
            for j in range(i, len(arr)):
                prod *= arr[j]
                
                max_product = max(max_product, prod)
                
        return max_product