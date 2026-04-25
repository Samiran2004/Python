"""
np.delete(array, index, axis=None)

"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

new_arr = np.delete(arr, 0, axis=None)

print(arr)
print(new_arr)