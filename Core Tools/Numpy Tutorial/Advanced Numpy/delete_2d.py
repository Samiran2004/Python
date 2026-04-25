import numpy as np

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

new_arr_2d = np.delete(arr_2d, 0, axis=0)

print(arr_2d)
print(new_arr_2d)