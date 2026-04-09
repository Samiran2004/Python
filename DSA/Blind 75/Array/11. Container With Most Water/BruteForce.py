from typing import List


class BruteForceSolution:
    def maxArea(self, height: List[int]):
        res = 0
        
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        
        return res