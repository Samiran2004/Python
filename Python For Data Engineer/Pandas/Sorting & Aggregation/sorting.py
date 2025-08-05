import pandas as pd


# Sorting data in one column....

# df.sort(by="Column name", True/False, inplace=True)

data = {
    "name": ["Arun", "Varun", "Tarun"],
    "age": [60, 22, 30],
    "salary": [10000, 20000, 30000]
}

data_frame = pd.DataFrame(data=data)

print(data_frame)

data_frame.sort_values(by="age", ascending=False, inplace=True)
print("Sorted age by decening...")
print(data_frame)