import pandas as pd
import numpy as np

# Loading dataset
df = pd.read_csv("./data/datasets/tawfikelmetwally/employee-dataset/versions/1/Employee.csv")

print(df.columns)

# Checking missing values...
print("Missing values in each column: ")
print(df.isnull().sum())

print(df['PaymentTier'])