import numpy as np

prices = np.array([100, 200, 300])

discount = 10 #Scalar single value

final_prices = prices - (prices * discount / 100)

print(final_prices)