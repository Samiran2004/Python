from typing import List


class BruteForceSolution:
    def reverseArray(self, arr: List[int]):
        resultArray = [0]*len(arr)

        for i in range(len(arr)):
            resultArray[i] = arr[len(arr) - i - 1]

        for i in range(len(resultArray)):
            arr[i] = resultArray[i]