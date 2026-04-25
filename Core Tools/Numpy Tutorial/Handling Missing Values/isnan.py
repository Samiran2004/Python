# np.isnan(array)

import numpy as np

arr = np.array([1, 2, 3, np.nan, 4, np.nan])

print(np.isnan(arr)) #[False False False  True False  True]

#We can't compare it directly...
# print(np.nan == np.nan)