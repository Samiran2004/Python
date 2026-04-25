from typing import List
def getRow(rowIndex: int)-> List[int]:
    res = [1]
    if rowIndex == 0:
        return res
    for i in range(rowIndex):
        next_row = [0] * (len(res) + 1)
        for j in range(len(res)):
            next_row[j] += res[j]
            next_row[j + 1] += res[j]
        res = next_row
    return res

numRows = int(input("Enter the number of rows: "))
arr = getRow(rowIndex=numRows)
print(arr)
