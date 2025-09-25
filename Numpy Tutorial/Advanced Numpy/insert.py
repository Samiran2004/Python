"""
np.insert(array, index, value, axis=None)
array -> original array
index
value
axis
axis = 0, row-wise
axis = 1, column-wise
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

new_arr = np.insert(arr, 2, 99)

print(f"Previous array: {arr}")
print(f"New array: {new_arr}")