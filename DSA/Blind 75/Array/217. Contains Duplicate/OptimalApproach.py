from typing import List


class OptimalApproachSolution:
    def containsDuplicate(self, arr: List[int]):
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i] == arr[i + 1]:
                return True
        return False