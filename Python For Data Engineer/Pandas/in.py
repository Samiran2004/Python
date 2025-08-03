import pandas as pd

# path = "/home/samiransamanta/Python/Python For Data Engineer/Pandas/sample_Data.json"
path = "Pandas/sales_data_sample1.csv"

df = pd.read_csv(path, encoding="latin1")

print("Display the info of data set...")
print(df.info())