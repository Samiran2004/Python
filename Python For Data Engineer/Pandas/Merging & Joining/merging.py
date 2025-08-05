import pandas as pd

# df.merge(dataframe1, dataframe2, on="Common column name", how="join type")

customer_dataframe = pd.DataFrame({
    "CustomerId": [1, 2, 3],
    "Name": ["Ramesh", "Suresh", "Kalpesh"]
})

order_dataframe = pd.DataFrame({
    "CustomerId": [1, 2, 4],
    "Order_amt": [150, 350, 450]
})

# mergedData = pd.merge(customer_dataframe, order_dataframe, on="CustomerId", how="inner")
# mergedData = pd.merge(customer_dataframe, order_dataframe, on="CustomerId", how="outer")
# mergedData = pd.merge(customer_dataframe, order_dataframe, on="CustomerId", how="left")
mergedData = pd.merge(customer_dataframe, order_dataframe, on="CustomerId", how="right")
print(mergedData)