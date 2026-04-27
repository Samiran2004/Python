import math

class BruteForceSolution:
    def closest_number(self, n, m):
        closest = 0
        min_difference = float('inf')

        for i in range(n - abs(m), n + abs(m) + 1):
            if i % m == 0:
                difference = abs(n - i)
    
                if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
                    closest = i
                    min_difference = difference
        return closest