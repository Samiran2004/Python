from typing import List


class UsingSinglePointerApproachSolution:
    def reverseArray(self, arr: List[int]):
        n = len(arr)
        for i in range(n // 2):
            temp = arr[i]
            arr[i] = arr[n - i - 1]
            arr[n - i - 1] = temp