from typing import List


class BetterApproachSolution:
    def maxArea(self, height: List[int]):
        res = 0
        left, right = 0, len(height) - 1
        
        while (left < right):
            area = (right - left) * min(height[left], height[right])
            res = max(area, res)
            
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                right -= 1
        return res