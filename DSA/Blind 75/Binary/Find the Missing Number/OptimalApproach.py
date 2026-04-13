from typing import List

class OptimalApproachSolution:
    def missingNum(self, arr: List[int]) -> int:
        n = len(arr)
        
        total_sum = sum(arr)
        
        expected_sum = n * (n + 1) // 2
        
        return expected_sum - total_sum