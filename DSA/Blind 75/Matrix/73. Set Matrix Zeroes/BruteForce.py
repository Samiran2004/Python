from typing import List


class BruteForceSolution:
    def setZeroes(self, matrix: List[List[int]]):
        row = len(matrix)
        column = len(matrix[0])
        
        # Step 1: Mark rows and columns
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    for k in range(column):
                        if matrix[i][k] != 0:
                            matrix[i][k] = float('inf')
                    
                    for k in range(row):
                        if matrix[k][j] != 0:
                            matrix[k][j] = float('inf')
        
        # Step 2: Convert 'inf' to 0
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0