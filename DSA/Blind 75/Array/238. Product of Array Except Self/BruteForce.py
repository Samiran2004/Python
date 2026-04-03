from typing import List


class BruteForceSolution:
    def productExceptSelf(self, arr: List[int]):
        n = len(arr)
        res = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j:
                    res[i] *= arr[j]
        return res