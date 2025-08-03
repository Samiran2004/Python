import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Samiran", "Jhon", "Jene", "Victor", "Raj", "Simran"],
    "Age": [28, 27, 30, 40, 29, 60, 32, 45],
    "Salary": [50000, 40000, 60000, 30000, 45000, 49000, 70000, 48000],
    "Performance_Score": [85, 90, 78, 92, 88, 95, 89, 80]
}

data_frame = pd.DataFrame(data=data)

print("Sample Dataframe")
print(data_frame)

print("Descriptive Stastics")
print(data_frame.describe())