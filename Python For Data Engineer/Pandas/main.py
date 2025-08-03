import pandas as pd

# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("kyanyoga/sample-sales-data")

# print("Path to dataset files:", path)

# Read data from CSV file into a dataframe
# df = pd.read_csv("/home/samiransamanta/Python/Python For Data Engineer/Pandas/sales_data_sample1.csv", encoding="latin1")

# df = pd.read_excel("/home/samiransamanta/Python/Python For Data Engineer/Pandas/SampleSuperstore.xlsx", engine="openpyxl")
# print(df.head())

df = pd.read_json("Pandas/sample_Data.json")