import pandas as pd

data = {
    "Name": ["Arun", "Varun", "Tarun", "Karun", "Narun"],
    "Age": [18, 32, 54, 34, 40],
    "Salary": [50000, 60000, 45000, 52000, 48000]
}

dataFrame = pd.DataFrame(data=data)

print(dataFrame)

groupedDate = dataFrame.groupby(by="Age")["Salary"].sum()
print(groupedDate)