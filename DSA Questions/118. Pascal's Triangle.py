from typing import List
def generate(numRows: int)-> List[List[int]]:
    if numRows == 0:
        return [[]]
    res = [[1]]
    for i in range(numRows - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res

numRows = int(input("Enter the number of rows: "))
arr = generate(numRows=numRows)
print(arr)
