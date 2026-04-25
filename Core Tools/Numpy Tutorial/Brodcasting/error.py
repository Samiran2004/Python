import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]]) # 2x3 matrix

vector = np.array([1, 2])

result = arr + vector # Give value error...

print(result)