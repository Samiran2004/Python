from typing import List


class BetterApproachSolution:
    def setZeroes(self, matrix: List[List[int]]):
        row = len(matrix)
        column = len(matrix[0])
        
        row_marked = [0] * row
        column_marked = [0] * column
        
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    row_marked[i] = 1
                    column_marked[j] = 1
        
        for i in range(row):
            for j in range(column):
                if row_marked[i] == 1 or column_marked[j] == 1:
                    matrix[i][j] = 0