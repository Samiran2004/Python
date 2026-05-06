from typing import List


class UsingTwoPointersApproachSolution:
    def reverseArray(self, arr: List[int]):
        start = 0
        end = len(arr) - 1

        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1