from typing import List


class BruteForceSolution:
    def containsDuplicate(self, arr: List[int]):
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    return True
        return False