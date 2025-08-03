import pandas as pd

data = {
    "Name": ["Samiran", "Ram", "Shyam"],
    "Age": [10, 20, 30],
    "City": ["Nagpur", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data=data)

print(df)

df.to_csv("./save_output.csv", index=False)

df.to_json('./save_output.json', index=False)