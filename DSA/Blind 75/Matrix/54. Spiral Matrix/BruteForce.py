from typing import List

class BruteForceSolution:
    def spiralOrder(self, matrix: List[List[int]]):
        result = []
        
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            
            # 1. Top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # 2. Right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # 3. Bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # 4. Left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result