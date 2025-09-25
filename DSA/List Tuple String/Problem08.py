def maximumWealth(accounts):
    row = len(accounts)
    column = len(accounts[0])
    max_wealth = 0
    for i in range(row):
        curr_wealth = 0
        for j in range(column):
            curr_wealth += accounts[i][j]

        max_wealth = max(curr_wealth, max_wealth)

    return max_wealth

row = int(input("Enter the size of the row of the matrix: "))
column = int(input("Enter the size of the column of the matrix: "))
arr = []

for i in range(0, row):
    columnData = []
    for j in range(0, column):
        data = int(input("Enter data: "))
        columnData.append(data)
    arr.append(columnData)

print(arr)
