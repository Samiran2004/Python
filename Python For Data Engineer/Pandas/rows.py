import pandas as pd

path = "Pandas/sales_data_sample1.csv"

df = pd.read_csv(path, encoding="latin1")

print(df.head(5))

print(df.tail(5))