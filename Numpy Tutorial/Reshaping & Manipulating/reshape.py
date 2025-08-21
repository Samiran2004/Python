"""
reshape(rows, columns) specify new shape
if dimensions match

reshapping does not create copy... it returns a view...
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)

print(f"Array: {arr}")
print(f"Reshaped array: {reshaped_arr}")