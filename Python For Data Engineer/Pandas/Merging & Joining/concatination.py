# pd.concate([df1, df2], axis=0, ignore_index=True)

import pandas as pd

df_region1 = pd.DataFrame({
    "CustomerId": [1, 2],
    "Name": ["Gopal", "Raju"]
})

df_region2 = pd.DataFrame({
    "CustomerId": [3, 4],
    "Name": ["Shyam", "Babu Rao"]
})

# Vertical concatination...
# concate_data = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)

# Horizontally concatination...
concate_data = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print(concate_data)