import numpy as np

"""
slicing

array[start:stop:step]

arr[start:end], start to end - 1
"""

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:5]) # index 1 to 4

print(arr[:4]) # index 0 to 3

print(arr[::2]) # every 2nd element

print(arr[::-1]) # reverse the array