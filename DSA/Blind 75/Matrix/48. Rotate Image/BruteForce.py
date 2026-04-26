from typing import List


class BruteForceSolution:
    def rotate(self, matrix: List[List[int]])-> List[List[int]]:
        n = len(matrix)
        
        ans = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                ans[j][n - 1 - i] = matrix[i][j]
        
        return ans