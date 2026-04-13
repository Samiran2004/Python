from typing import List


class BruteForceSolution:
    def missingNum(self, arr: List[int]):
        for i in range(1, len(arr) + 1):
            found = False
            for j in range(len(arr)):
                if i == arr[j]:
                    found = True
                    break
            if not found:
                return i
        
        return -1