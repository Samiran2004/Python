# Fancy indexing

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[[0, 2, 4]])

# boolien masking...
print(arr[arr > 25])