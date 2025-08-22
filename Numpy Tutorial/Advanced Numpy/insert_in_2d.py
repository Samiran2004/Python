import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Insert a new row at index 1

new_arr_2d = np.insert(arr_2d, 1, [5, 6, 7], axis=0)

print(arr_2d)
print(new_arr_2d)